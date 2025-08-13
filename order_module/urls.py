from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add-cart/<int:car_id>', views.add_to_cart, name='add_to_cart'),
    path('remove-cart/<int:car_id>', views.remove_from_cart, name='remove_from_cart'),
]
