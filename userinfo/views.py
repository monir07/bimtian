from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View


# Create your views here.
class CustomPermissionMixin(PermissionRequiredMixin):
    permission_required = ""
    allowed_roles=['ADMIN']
    def has_permission(self) -> bool:
        if self.request.user.groups.exists():
            groups = self.request.user.groups.all()
            for group in groups:
                if group.name in self.allowed_roles:
                    return True
            return False
        return False


class CommonMixin(SuccessMessageMixin, LoginRequiredMixin, CustomPermissionMixin):
    permission_required = ""
    permission_denied_message = "You don't have permission"
    title = ""

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['title'] = self.title
        return data


class LoginView(View):
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, self.template_name, context)


class SingupView(View):
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, self.template_name, context)