from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    '''
    Класс-модель воспоминание, представляет из себя 
    данные об месте в котором был пользователя
    '''
    title = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = "Воспоминание"
        verbose_name_plural = "Воспоминания"

    def __repr__(self):
        return f'Воспоминание юзера {self.owner.id} - {self.title}'