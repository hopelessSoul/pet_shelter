import base64
import datetime
import uuid

import requests
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from pets_app.models import Pet
from pets_app.utils.serializers.serializers import PetSerializer

from pets_app.forms import PetForm


class PetsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        qs = Pet.objects.filter(archived=False).all()
        data = PetSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class AddPetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        new_pet, created = Pet.objects.get_or_create(**data)
        qs = Pet.objects.get(**data)
        serialized_data = PetSerializer(qs).data
        if not created:
            return Response({"msg": "Питомец уже существует", "pet": serialized_data}, status=status.HTTP_302_FOUND)
        return Response({"msg": "Питомец успешно создан", "pet": serialized_data}, status=status.HTTP_201_CREATED)


class UpdatePetInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            data = request.data
            pet = Pet.objects.get(pk=pk)
            pet.age = int(data['age'])
            pet.height = float(data['height'])
            pet.weight = float(data['weight'])
            pet.nickname = data['nickname']
            pet.special_signs = data['special_signs']
            pet.save()
            serialized_data = PetSerializer(pet).data
            return Response({"msg": "Питомец успешно обновлен", "pet": serialized_data}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"error_msg": ex}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        if User.is_superuser:
            try:
                pet = Pet.objects.get(pk=pk)
                pet.archived = True
                pet.save()
                return Response({"msg": "Питомец успешно удален"}, status=status.HTTP_200_OK)
            except Exception as ex:
                return Response({"error": ex}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Home(View):
    def get(self, request):
        pets = requests.get('http://127.0.0.1:8000/api/pets-info').json()
        return render(request, 'pets/home.html', {'pets': pets})


class CreatePetView(CreateView):
    template_name = 'pets/add-pet.html'
    model = Pet
    fields = "nickname", "age", "arriving_date", "weight", "height", "special_signs"
    success_url = reverse_lazy("pets:home")
