from django.views.generic import ListView, DetailView
from .models import Car


class CarListView(ListView):
    model = Car
    template_name = 'car_module/car-list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_module/car-detail.html'
    context_object_name = 'car'
