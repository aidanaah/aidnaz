from django.urls import path
from . import views

urlpatterns = [
    path('', views.finelle_wdress, name='finelle_wdress'),
]
