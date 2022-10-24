from django.urls import path, include
from .views import *
urlpatterns = [
    path('dashboard', AdminDashboard.as_view(), name='dashboard'),
    # --- user info urls --- 
    path('user-info-form/', UserInfoCreateView.as_view(), name='user_info_form'),
    path('present-address-form/', UserInfoCreateView.as_view(model=PresentAddress, form_class=PresentAddressForm, title="Your Present Address"), name='present_address_form'),
    path('permanent-address-form/', UserInfoCreateView.as_view(model=PermanentAddress, form_class=PermanentAddressForm, title="Your Permanent Address"), name='permanent_address_form'),

    # --- user portfolio urls ---
    path('portfolio-info-form/', UserInfoCreateView.as_view(model=PortfolioInfo, form_class=PortfolioInfoForm, title="Portfolio Information Form"), name='portfolio_form'),
    path('portfolio-service-form/', UserInfoCreateView.as_view(model=Services, form_class=ServicesForm, title="My Professional Servises Form"), name='service_form'),
    path('portfolio-project-form/', UserInfoCreateView.as_view(model=Portfolio, form_class=PortfolioForm, title="My Project Form"), name='project_form'),
    path('portfolio-education-form/', UserInfoCreateView.as_view(model=Education, form_class=EducationForm, title="Educational Information Form"), name='education_form'),
    path('portfolio-skill-form/', UserInfoCreateView.as_view(model=ProfessionalSkills, form_class=ProfessionalSkillsForm, title="Professional Skill Form"), name='skill_form'),
    path('portfolio-experience-form/', UserInfoCreateView.as_view(model=Experince, form_class=ExperinceForm, title="My Experience Form"), name='experience_form'),
    path('portfolio-feedback-form/', UserInfoCreateView.as_view(model=ClientFeedback, form_class=ClientFeedbackForm, title="Client Feedback Form"), name='feedback_form'),
]