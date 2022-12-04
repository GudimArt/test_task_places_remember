from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save  # add this
from django.contrib.auth.models import User


class UserProfile(models.Model):
    '''
    Расширение пользователя с целью хранения аватара
    '''

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE,)
    avatar = models.URLField(blank=True)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'Профиль пользователя {self.user.id}'


class Memory(models.Model):
    '''
    Класс-модель воспоминание, представляет из себя
    данные об месте в котором был пользователя
    '''

    title = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=1000)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Воспоминание"
        verbose_name_plural = "Воспоминания"

    def __repr__(self):
        return f'Воспоминание юзера {self.owner} - {self.title}'
