from django.urls import path, include
from . import views

app_name = "pets"

urlpatterns = [
    path('api/pets-info', views.PetsView.as_view(), name='pets_view'),
    path('api/add-pet', views.AddPetView.as_view(), name='add_pet'),
    path('api/update-pet/<int:pk>', views.UpdatePetInfoView.as_view(), name='update_pet'),

    path('home', views.Home.as_view(), name='home'),
    path('add-pet', views.CreatePetView.as_view(), name="add-pet"),
]
