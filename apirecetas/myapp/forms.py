from django import forms
from .models import Recipes


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "ingredients", "preparation", "people", "onMenu"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "preparation": forms.Textarea(attrs={"class": "form-control"}),
            "people": forms.NumberInput(attrs={"class": "form-control"}),
            "onMenu": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
