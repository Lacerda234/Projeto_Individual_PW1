from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from pages_app.models import Animal, Usuario

def home(request):
    return render(request, 'pages_app/home.html')

#views referentes a parte de animais
class AnimalList(ListView):
    model = Animal
    queryset = Animal.objects.all()

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('pages_app:list')

class AnimalUpdate(UpdateView):
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('pages_app:list')

class AnimalDetail(DetailView):
    queryset = Animal.objects.all()

class AnimalDelete(DeleteView):
    queryset = Animal.objects.all()
    success_url = reverse_lazy('pages_app:list')

#viwes referentes a parte de usuários
class UsuarioList(ListView):
    model = Usuario
    queryset = Usuario.objects.all()

class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('pages_app:listUser')

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('pages_app:listUser')

class UsuarioDetail(DetailView):
    queryset = Usuario.objects.all()

class UsuarioDelete(DeleteView):
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('pages_app:listUser')