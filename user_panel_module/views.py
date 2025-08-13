from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from user_panel_module.forms import EditProfileModelForm


@method_decorator(login_required, name='dispatch')
class EditUserProfilePageView(View):
    def get(self, request):
        edit_form = EditProfileModelForm(instance=request.user)
        context = {
            'form': edit_form,
            'current_user': request.user
        }
        return render(request, 'user_panel_module/user-panel.html', context)

    def post(self, request):
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
        context = {
            'form': edit_form,
            'current_user': request.user
        }
        return render(request, 'user_panel_module/user-panel.html', context)
