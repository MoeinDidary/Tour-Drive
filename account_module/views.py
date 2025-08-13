from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views import View
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User
from utils.email_service import send_email


class RegisterFormView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'account_module/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get("username")
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')

            if User.objects.filter(username__iexact=username).exists():
                register_form.add_error('username', 'The Username Entered Is A Duplicate.')
            elif User.objects.filter(email__iexact=user_email).exists():
                register_form.add_error('email', 'The Email Entered Is A Duplicate.')
            else:
                # کاربر غیرفعال ساخته میشه
                new_user = User(
                    username=username,
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()

                # ارسال ایمیل فعال‌سازی
                send_email(
                    'Activate Your Account',
                    new_user.email,
                    {'user': new_user},
                    'emails/activate_account.html'
                )

                return redirect(reverse('show_login'))

        return render(request, 'account_module/register.html', {'register_form': register_form})


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)  # کد جدید برای امنیت
                user.save()
                return redirect(reverse('show_login'))
            else:
                # اگه قبلاً فعال شده
                return redirect(reverse('show_login'))
        raise Http404


class LoginFormView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account_module/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()

            if user:
                if not user.is_active:
                    login_form.add_error(None, 'Your account is not activated. Please check your email.')
                elif user.check_password(user_password):
                    login(request, user)
                    return redirect('show_home')
                else:
                    login_form.add_error('password', 'The Password Entered Is Incorrect.')
            else:
                login_form.add_error('email', 'No Email With These Details Was Found.')

        return render(request, 'account_module/login.html', {'login_form': login_form})


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('show_login')

    def post(self, request):
        logout(request)
        return redirect('show_login')
