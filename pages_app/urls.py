from django.urls import path

from pages_app import views

from . import views

app_name = 'pages_app'

urlpatterns = [
    #views para a parte de animais
    path('', views.home, name='home'),
    path('listAnimal', views.AnimalList.as_view(), name='list'),
    path('createAnimal/', views.AnimalCreate.as_view(), name='createAnimal'),
    path('updateAnimal/<int:pk>/', views.AnimalUpdate.as_view(), name='updateAnimal'),
    path('detailAnimal/<int:pk>/', views.AnimalDetail.as_view(), name='detailAnimal'),
    path('deleteAnimal/<int:pk>/', views.AnimalDelete.as_view(), name='deleteAnimal'),

    #views para a parte de usuarios
    path('listaUsuarios/', views.UsuarioList.as_view(), name='listUser'),
    path('createUser/', views.UsuarioCreate.as_view(), name='createUser'),
    path('updateUser/<int:pk>/', views.UsuarioUpdate.as_view(), name='updateUser'),
    path('detailUser/<int:pk>/', views.UsuarioDetail.as_view(), name='detailUser'),
    path('deleteUser/<int:pk>/', views.UsuarioDelete.as_view(), name='deleteUser'),
]