from django.shortcuts import render
from .models import Wdress

def finelle_wdress(request):
    wdresses = Wdress.objects.all()
    context = {
        'wdresses': wdresses
    }
    return render(request, "finelle_wdress.html", context)
