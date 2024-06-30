from django.contrib import admin

from pets_app.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    fields = ('nickname', 'age', 'arriving_date', 'weight', 'height', 'special_signs')
