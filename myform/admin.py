from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'family_name', 'age', 'selection', 'nationality', 'date_of_birth')
    search_fields = ('name', 'family_name')
