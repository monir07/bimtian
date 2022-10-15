from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View, generic
from .form import *
from django.contrib.auth.models import User
from django.db import transaction
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

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


class LoginView(SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'indent/material_demand/form.html'
    success_message = "Information added successfully"
    title = "Add Material Demand"
    # success_url = reverse_lazy("material_demand_list")
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, self.template_name, context)


class SingupView(generic.CreateView):
    model = User
    form_class = NewUserForm
    success_message = "User created successfully"
    title = "New user signup"
    template_name = 'authentication/signup.html'
    uccess_url = reverse_lazy("login")

    def form_valid(self, form, *args, **kwargs):
        with transaction.atomic():
            self.object.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['form'] = self.get_form()
        return context