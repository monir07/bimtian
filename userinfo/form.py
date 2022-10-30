from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2", "first_name", "last_name")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user


class UserInfoForm(forms.ModelForm):
	date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

	class Meta:
		model = UserInfo
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')
		labels = {
            "ecp": "Emergency Contact Person (ECP)",
            "contact_no_ecp": "Contact Number (ECP)",
            "relation_with_ecp": "Relation With ECP",
        }

class PortfolioInfoForm(forms.ModelForm):
	class Meta:
		model = PortfolioInfo
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class ServicesForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class PortfolioForm(forms.ModelForm):
	class Meta:
		model = Portfolio
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')		


class EducationForm(forms.ModelForm):
	class Meta:
		model = Education
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class ProfessionalSkillsForm(forms.ModelForm):
	class Meta:
		model = ProfessionalSkills
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')


class ExperinceForm(forms.ModelForm):
	class Meta:
		model = Experince
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class ClientFeedbackForm(forms.ModelForm):
	contract_start = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
	contract_end = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
	class Meta:
		model = ClientFeedback
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')


class PresentAddressForm(forms.ModelForm):
	class Meta:
		model = PresentAddress
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class PermanentAddressForm(forms.ModelForm):
	class Meta:
		model = PermanentAddress
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')


class ContactRequestForm(forms.ModelForm):
	class Meta:
		model = ContactRequest
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class PermanentAddressForm(forms.ModelForm):
	class Meta:
		model = PermanentAddress
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')

class PresentAddressForm(forms.ModelForm):
	class Meta:
		model = PresentAddress
		fields = '__all__'
		exclude = ('user', 'created_by', 'updated_by', 'created_at', 'updated_at')
