from django.urls import path
from . import views

urlpatterns = [
    path('list-car', views.CarListView.as_view(), name='show_list_cars'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='show_detail_car')

]
