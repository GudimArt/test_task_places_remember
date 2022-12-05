from django.shortcuts import render, redirect
from .models import Memory
from .forms import AddMemoryFrom


def home(request):
    if request.user.is_authenticated:
        form = AddMemoryFrom()
        user_memory = Memory.objects.filter(owner=request.user)
    return render(request, 'places_remember_app/home.html', locals())


def add_memory(request):
    if request.method == 'POST':
        form = AddMemoryFrom(request.POST)
        if form.is_valid():
            try:
                memory = form.save(commit=False)
                memory.owner = request.user
                memory.save()
                return redirect('/')
            except:
                form.add_error(None, 'Ошибка добавления воспоминания')
    else:
        form = NameForm()
    return render(request, 'places_remember_app/home.html', {'form': form})
