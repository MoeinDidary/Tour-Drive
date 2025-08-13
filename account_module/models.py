from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='avatar', upload_to='images', blank=True, null=True)
    email_active_code = models.CharField(verbose_name='email active code', max_length=100)
    about_user = models.TextField(verbose_name='about user', null=True, blank=True)
    address = models.TextField(verbose_name='address', null=True, blank=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = 'users'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        else:
            return self.email
