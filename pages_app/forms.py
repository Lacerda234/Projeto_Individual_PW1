from django import forms

from pages_app.models import Animal, Usuario

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'