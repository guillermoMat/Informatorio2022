from .base import *

DEBUG = True
ALLOWED_HOSTS = []
# Hacer pip install msqlclient dentro del entorno


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'proyecto_info', # Reemplazar por el nombre de la base local creada en el Workbench
        'USER': 'root',
        'PASSWORD': 'sys64738', # Reemplazar por la contraseña de la base local creada en el Workbench
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'databaseName',
#         'USER': 'databaseUser',
#         'PASSWORD': 'databasePassword',
#         'HOST': 'localhost',
#         'PORT': 'portNumber',
#     }