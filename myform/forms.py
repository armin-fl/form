from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'family_name', 'age', 'selection', 'nationality', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.HiddenInput()  # We'll handle this with JavaScript
        }
