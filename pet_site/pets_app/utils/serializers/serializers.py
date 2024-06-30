from rest_framework.serializers import ModelSerializer

from pets_app.models import Pet


class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ['nickname', 'age', 'arriving_date', 'weight', 'height', 'special_signs']
