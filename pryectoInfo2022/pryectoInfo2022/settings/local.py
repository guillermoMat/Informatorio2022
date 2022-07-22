from .base import *

DEBUG = True

# Hacer pip install msqlclient dentro del entorno
# Hacer pip install PyMySQL dentro del entorno

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'proyectoinfo', # Reemplazar por el nombre de la base local creada en el Workbench
        'USER': 'root',
        'PASSWORD': 'sys64738', # Reemplazar por la contraseña de la base local creada en el Workbench
        'HOST': 'localhost',
        'PORT': '3306',
    }
}