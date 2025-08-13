from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name='show_register'),
    path('login', views.LoginFormView.as_view(), name='show_login'),
    path('logout', views.LogoutView.as_view(), name='show_logout'),
    path('activate/<email_active_code>/', views.ActivateAccountView.as_view(), name='activate_account')

]
