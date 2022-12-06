from django import forms

from .models import Memory


class AddMemoryFrom(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'description']
