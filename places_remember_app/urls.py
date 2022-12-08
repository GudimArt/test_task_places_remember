from django.urls import path
from django.contrib.auth import views as authViews
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', authViews.LogoutView.as_view(), name='exit'),
    path('add_memory/', add_memory, name='add_memory'),
    path('del_memory/<int:id>', del_memory, name='del_memory'),

]
