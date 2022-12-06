from django.contrib import admin
from .models import Memory, UserProfile

admin.site.register(UserProfile)
admin.site.register(Memory)
