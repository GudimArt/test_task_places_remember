from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Memory
from .forms import AddMemoryFrom
from django.conf import settings


def home(request):
    api_key = settings.YANDEX_MAPS_API_STR
    if request.user.is_authenticated:
        form = AddMemoryFrom()
        user_memory = Memory.objects.filter(owner=request.user)
    return render(request, 'places_remember_app/home.html', locals())


def add_memory(request):
    api_key = settings.YANDEX_MAPS_API_STR
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddMemoryFrom(request.POST)
            if form.is_valid():
                memory = form.save(commit=False)
                memory.owner = request.user
                memory.save()
                return redirect('/')
            else:
                form.add_error(None, 'Ошибка добавления воспоминания')
                return render(request, 'places_remember_app/memory_edit.html', locals())
        else:
            form = AddMemoryFrom()
            return render(request, 'places_remember_app/memory_edit.html', locals())
    else:
        return HttpResponse("Вы НЕ авторизованы, чтобы добавить воспоминание")


def del_memory(request, id):
    if request.user.is_authenticated:
        memory = Memory.objects.get(id=id)
        memory.delete()
        return redirect('/')
    else:
        return HttpResponse("Вы НЕ авторизованы, чтобы удалить воспоминание")
