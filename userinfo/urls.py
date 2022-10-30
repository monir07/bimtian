from django.urls import path, include
from .views import *
urlpatterns = [
    path('dashboard', AdminDashboard.as_view(), name='dashboard'),
    path('portfolio-site/<int:pk>/', PortfolioHomeView.as_view(), name='portfolio_site'),
    # --- user info urls --- 
    path('user-info-form/', UserInfoCreateView.as_view(), name='user_info_form'),
    path('user-info-update/<int:pk>/', UserInfoUpdateView.as_view(), name='user_info_update'),
    path('portfolio-list/', UserInfoListView.as_view(), name='profile_list'),

    # PRESENT ADDRESS
    path('present-address-form/', UserInfoCreateView.as_view(model=PresentAddress, form_class=PresentAddressForm, title="Your Present Address", success_url="present_address_list"), name='present_address_form'),
    
    path('present-address-update/<int:pk>/', UserInfoUpdateView.as_view(model=PresentAddress, form_class=PresentAddressForm, title="Update Present Address", success_url="present_address_list"), name='present_address_update'),

    path('present-address-list/', UserInfoListView.as_view(model=PresentAddress, title="Present Address", template_name = 'user_info/portfolio_site/present_address.html'), name='present_address_list'),
    
    # PERMANENT_ADDRESS
    path('permanent-address-form/', UserInfoCreateView.as_view(model=PermanentAddress, form_class=PermanentAddressForm, title="Your Permanent Address", success_url="permanent_address_list"), name='permanent_address_form'),
    
    path('permanent-address-update/<int:pk>/', UserInfoUpdateView.as_view(model=PermanentAddress, form_class=PermanentAddressForm, title="Update Permanent Address", success_url="permanent_address_list"), name='permanent_address_update'),
    
    path('permanent-address-list/', UserInfoListView.as_view(model=PermanentAddress, title="Permanent Address", template_name = 'user_info/portfolio_site/permanent_address.html'), name='permanent_address_list'),

    # --- user portfolio urls ---
    # PORTFOLIO INFORMATION
    path('portfolio-info-form/', UserInfoCreateView.as_view(model=PortfolioInfo, form_class=PortfolioInfoForm, title="Portfolio Information Form", success_url="portfolio_info_list"), name='portfolio_form'),

    path('portfolio-info-update/<int:pk>/', UserInfoUpdateView.as_view(model=PortfolioInfo, form_class=PortfolioInfoForm, title="Update Portfolio Information", success_url="portfolio_info_list"), name='portfolio_info_update'),

    path('portfolio-info-list/', UserInfoListView.as_view(model=PortfolioInfo, title="Portfolio Information List", template_name = 'user_info/portfolio_site/portfolio_info_list.html'), name='portfolio_info_list'),
    
    # SERVICE INFORMATION
    path('portfolio-service-form/', UserInfoCreateView.as_view(model=Services, form_class=ServicesForm, title="My Professional Servises Form", success_url="service_list"), name='service_form'),

    path('portfolio-service-update/<int:pk>/', UserInfoUpdateView.as_view(model=Services, form_class=ServicesForm, title="Update Service Information", success_url="service_list"), name='sevice_info_update'),

    path('portfolio-service-list/', UserInfoListView.as_view(model=Services, title="My Professional Servises", template_name = 'user_info/portfolio_site/services_list.html'), name='service_list'),
    
    # PROJECT INFORMATION
    path('portfolio-project-form/', UserInfoCreateView.as_view(model=Portfolio, form_class=PortfolioForm, title="My Project Form", success_url="project_list"), name='project_form'),
    
    path('portfolio-project-update/<int:pk>/', UserInfoUpdateView.as_view(model=Portfolio, form_class=PortfolioForm, title="Update Project Information", success_url="project_list"), name='project_info_update'),

    path('portfolio-project-list/', UserInfoListView.as_view(model=Portfolio, title="My Professional Projects", template_name = 'user_info/portfolio_site/portfolio_list.html'), name='project_list'),

    # EDUCATION INFORMATION
    path('portfolio-education-form/', UserInfoCreateView.as_view(model=Education, form_class=EducationForm, title="Educational Information Form", success_url="education_list"), name='education_form'),

    path('portfolio-education-update/<int:pk>/', UserInfoUpdateView.as_view(model=Education, form_class=EducationForm, title="Update Education Information", success_url="education_list"), name='education_info_update'),

    path('portfolio-education-list/', UserInfoListView.as_view(model=Education, title="My Professional Degree", template_name = 'user_info/portfolio_site/education_list.html'), name='education_list'),

    # SKILL INFORMATION
    path('portfolio-skill-form/', UserInfoCreateView.as_view(model=ProfessionalSkills, form_class=ProfessionalSkillsForm, title="Professional Skill Form", success_url="skill_list"), name='skill_form'),
    
    path('portfolio-skill-update/<int:pk>/', UserInfoUpdateView.as_view(model=ProfessionalSkills, form_class=ProfessionalSkillsForm, title="Update Skill Information", success_url="skill_list"), name='skill_info_update'),

    path('portfolio-skill-list/', UserInfoListView.as_view(model=ProfessionalSkills, title="My Professional Skill", template_name = 'user_info/portfolio_site/skill_list.html'), name='skill_list'),

    # EXPERIENCE INFORMATION
    path('portfolio-experience-form/', UserInfoCreateView.as_view(model=Experince, form_class=ExperinceForm, title="My Experience Form", success_url="experience_list"), name='experience_form'),
    
    path('portfolio-experience-update/<int:pk>/', UserInfoUpdateView.as_view(model=Experince, form_class=ExperinceForm, title="Update Experience Information", success_url="experience_list"), name='experience_info_update'),

    path('portfolio-experience-list/', UserInfoListView.as_view(model=Experince, title="My Professional Experience", template_name = 'user_info/portfolio_site/experience_list.html'), name='experience_list'),

    # FEEDBACK INFORMATION
    path('portfolio-feedback-form/', UserInfoCreateView.as_view(model=ClientFeedback, form_class=ClientFeedbackForm, title="Client Feedback Form", success_url="feedback_list"), name='feedback_form'),
    
    path('portfolio-feedback-update/<int:pk>/', UserInfoUpdateView.as_view(model=ClientFeedback, form_class=ClientFeedbackForm, title="Update Feedback Information", success_url="feedback_list"), name='feedback_info_update'),

    path('portfolio-feedback-list/', UserInfoListView.as_view(model=ClientFeedback, title="My Professional Feedback", template_name = 'user_info/portfolio_site/feedback_list.html'), name='feedback_list'),
    
]