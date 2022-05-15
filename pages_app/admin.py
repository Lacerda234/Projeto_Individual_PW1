from django.contrib import admin
from .models import Usuario
from .models import Animal

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Animal)