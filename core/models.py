from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _


# Create your models here.
# class Usuario(models.Model):
#     nickname = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nickname

class CustomUser(AbstractUser):
    # Outros campos personalizados, se houver
    # ...

    # Defina o related_name para evitar conflitos
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set',
    )