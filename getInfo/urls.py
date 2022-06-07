from django.urls import path
from getInfo.views import *


urlpatterns = [
    path('', inicio),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('universidades/', universidades),
]