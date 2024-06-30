from django import forms

from pets_app.models import Pet


class PetForm(forms.ModelForm):
    arriving_date = forms.CharField()
    weight = forms.FloatField()
    height = forms.FloatField()

    class Meta:
        model = Pet
        fields = "nickname", "age", "arriving_date", "weight", "height", "special_signs"
