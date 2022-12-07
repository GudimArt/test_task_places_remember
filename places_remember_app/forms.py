from django import forms

from .models import Memory


class AddMemoryFrom(forms.ModelForm):
    title = forms.CharField(
        label="Название", widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        label="Комментарий", widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 10rem;"}))
    address = forms.CharField(
        label="Адрес", widget=forms.TextInput(attrs={"class": "form-control", 'id': "id_address"}))

    class Meta:
        model = Memory
        fields = ['title', 'description', 'address']
