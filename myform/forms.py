from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'family_name', 'age', 'selection', 'nationality', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'form-control border ' }),
            'family_name': forms.TextInput(attrs={'id': 'family_name', 'class': 'form-control border'}),
            'age': forms.NumberInput(attrs={'id': 'age', 'class': 'form-control border'}),
            'selection': forms.Select(attrs={'id': 'selection', 'class': 'form-control border'}),
            'nationality': forms.CheckboxInput(attrs={'id': 'nationality', 'class': 'form-check-input ' }),
            'date_of_birth': forms.HiddenInput()  # This will remain hidden and handled by JavaScript
        }
