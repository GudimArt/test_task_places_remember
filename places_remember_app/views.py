from django.shortcuts import render
from .models import Memory


def home(request):
    if request.user.is_authenticated:
        user_memory = Memory.objects.filter(owner=request.user)
    return render(request, 'places_remember_app/home.html', locals())
