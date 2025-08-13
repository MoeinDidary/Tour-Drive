from django.db import models

from account_module.models import User


class Car(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=100)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    capacity = models.PositiveIntegerField(verbose_name='Capacity')
    driver_name = models.CharField(verbose_name='Drive Name', max_length=100, blank=True, null=True)
    route = models.CharField(verbose_name='Route', max_length=200, blank=True, null=True)
    price_per_hour = models.DecimalField(verbose_name='Price Per Hour', max_digits=8, decimal_places=2)
    available = models.BooleanField(verbose_name='Available', default=True)
    image = models.ImageField(verbose_name='Image', upload_to='uploads/cars', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Create Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.name} - {self.capacity} seats"
