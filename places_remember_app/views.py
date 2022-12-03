from django.shortcuts import render


def home(request):
    return render(request, 'places_remember_app/home.html')
