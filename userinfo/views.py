from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View, generic
from django.db.models import Q,Count, Sum
from .form import *
from django.contrib.auth.models import User
from django.db import transaction
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType

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
class CustomLogEntry():
    def log_change(self, request, object, message):        
        return LogEntry.objects.log_action(
            user_id=request.user.id,
            content_type_id=ContentType.objects.get_for_model(object).pk,
            object_id=object.id,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
            )
    def log_addition(self, request, object, message):
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )
    def log_deletion(self, request, object, message):
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=DELETION,
            change_message=message,
        )
            

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/login.html'
    success_url = reverse_lazy("dashboard")
    success_message = 'Login successfully'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        messages.success(self.request, self.success_message)
        log_obj = CustomLogEntry()
        log_obj.log_addition(self.request, form.get_user(), self.success_message)
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("User is authenticated")
            return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data())

class UserPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'authentication/password_change.html'
    title = 'Password change'
    success_message = 'Password Change successfully'
    
    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, self.success_message)
        log_obj = CustomLogEntry()
        log_obj.log_change(self.request, form.user, self.success_message)
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")
    def get(self, request, *args, **kwargs):
        logout(request)        
        return HttpResponseRedirect(self.next_page)

class SingupView(generic.CreateView):
    model = User
    form_class = NewUserForm
    success_message = "User created successfully"
    title = "New user registration"
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form, *args, **kwargs):
        with transaction.atomic():
            form.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['form'] = self.get_form()
        return context

class AdminDashboard(generic.TemplateView):
    template_name = 'custom_admin/dashboard.html'
    title = 'Admin Dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class UserInfoCreateView(LoginRequiredMixin, generic.CreateView):
    # permission_required = 'indent.create_materialdemanditem'
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'user_info/form.html'
    success_message = "Information added successfully"
    title = "Add User Information"
    
    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        
        self.object.created_by = self.request.user
        with transaction.atomic():
            self.object.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)
    
    def get_success_url(self, **kwargs):  
        return reverse_lazy("dashboard") # kwargs = {'pk': self.kwargs.get('pk')}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class UserInfoListView(LoginRequiredMixin, generic.ListView):
    model = UserInfo
    context_object_name = 'items'
    template_name = 'user_info/user_info_list.html'
    title = "User Information List"
    # queryset = UserInfo.objects.all().order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)   
        context['title'] = self.title
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(user__id=self.request.user.id))                            
        return queryset


class UserInfoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'user_info/form.html'
    success_message = "Information updated successfully"
    title = "Update User Information"
    success_url = "profile_list" 

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.updated_by = self.request.user
        with transaction.atomic():
            self.object.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(reverse_lazy(self.success_url))
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['work'] = True
        return context

from django.contrib.auth import get_user_model
User = get_user_model()
class PortfolioHomeView(View):
    template_name = 'portfolio/home/index.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        context = {
            'user': user,
        }
        return render(request, self.template_name, context)