from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from PIL import Image
import os
User = get_user_model()


# User Information Model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='updated_%(class)ss', null=True, blank=True)

class CourseOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE  """
    DEMT = 'DEMT', 'Diploma In Engineering Marine Technology'
    DEST = 'DEST', 'Diploma In Engineering Shipbuilding Technology'
    MDEA = 'MDEA', 'Marine Diesel Engine Artificer'
    SF = 'SF', 'Ship Fabrication'
    SBW = 'SBW', 'Shipbuilding Welding'
    SBMD = 'SBMD', 'Shipbuilding and Mechanical Draftsmanship'


class CourseTypeOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE  """
    DIPLOMA = 'diploma', 'Diploma Engineering'
    TRADE = 'trade', 'Trade Course'


class EmploymentOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE  """
    EMPLOYED = 'employed', 'Employed'
    UNEMPLOYED = 'unemployed', 'Un-employed'
    BUSINESS = 'business', 'Business'

class ReligionOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    ISLAM = 'ISLAM', 'Islam'
    HINDU = 'HINDU', 'Hindu'
    CHRISTIAN = 'CHRISTIAN', 'Christian'
    BUDDHIST = 'BUDDHIST', 'Buddhist'
    OTHERS = 'OTHERS', 'Others'

class GenderOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female'
    OTHERS = 'OTHERS', 'Others'


class BloodGroupOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    A_POSITIVE = 'A+', 'A+'
    A_NEGATIVE = 'A-', 'A-'
    B_POSITIVE = 'B+', 'B+'
    B_NEGATIVE = 'B-', 'B-'
    O_POSITIVE = 'O+', 'O+'
    O_NEGATIVE = 'O-', 'O-'
    AB_POSITIVE = 'AB+', 'AB+'
    AB_NEGATIVE = 'AB-', 'AB-'

class MaritalOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    MARRIED = 'MARRIED', 'Married'
    SINGLE = 'SINGLE', 'Single'
    DIVORCED = 'DIVORCED', 'Divorced'


def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.png', '.gif']
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class UserInfo(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    course_type = models.CharField(max_length=100, choices= CourseTypeOptions.choices)
    course_name = models.CharField(max_length=25, choices= CourseOptions.choices)
    intake_name = models.CharField(max_length=25)
    bimt_passing_year = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()    
    religion = models.CharField(max_length=50, choices= ReligionOptions.choices)
    gendar = models.CharField(max_length=50, choices= GenderOptions.choices)
    blood_group = models.CharField(max_length=50, choices= BloodGroupOptions.choices)
    marital_status = models.CharField(max_length=50, choices= MaritalOptions.choices)    
    # emergency contact person.
    ecp = models.CharField(max_length=100, blank=True, null=True)
    # emergency contact person cell phone.
    contact_no_ecp = models.CharField(max_length=100, blank=True, null=True)
    # emergency contact person relation.
    relation_with_ecp = models.CharField(max_length=100, blank=True, null=True)
    

class PortfolioInfo(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio_info')
    employment_status = models.CharField(max_length=100, choices=EmploymentOptions.choices)
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)    
    phone_no = models.CharField(max_length=100)
    about_me = models.CharField(max_length=250)
    profile_img = models.ImageField(default = 'profile_img/default.jpg', upload_to='profile_img/', validators=[file_size], help_text="File size should be less than 2mb(.jpg/.png/.gif)")
    banner_image = models.ImageField(upload_to='banner_img/', validators=[file_size], help_text="File size should be less than 2mb(.jpg/.png/.gif)")
    footer_image = models.ImageField(upload_to='footer_img/', validators=[file_size], help_text="File size should be less than 2mb(.jpg/.png/.gif)")
    facebook_id = models.URLField(max_length=200)
    linked_id = models.URLField(max_length=200)
    github_id = models.URLField(max_length=200)
    cv_link = models.URLField(max_length=350)

    def save(self, *args, **kwargs):
        super(PortfolioInfo, self).save(*args, **kwargs)
        img = Image.open(self.profile_img.path)
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)


class Services(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_service')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=350)


class Portfolio(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_portfolio')
    project_name = models.CharField(max_length=150)
    project_img = models.URLField(max_length=350)
    preview_link = models.URLField(max_length=350)
    github_link = models.URLField(max_length=350)


class Education(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_education')
    degree_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    institute = models.CharField(max_length=250)
    start_year = models.IntegerField()
    passing_year = models.IntegerField()
    short_brief = models.TextField(max_length=350)


class ProfessionalSkills(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_skill')
    skill_logo = models.URLField(max_length=250)
    skill_name = models.CharField(max_length=100)


class Experince(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_experience')
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    join_year = models.IntegerField()
    resign_year = models.IntegerField()
    responsibility = models.TextField(max_length=350)
    company_logo = models.URLField(max_length=250)


class ClientFeedback(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_feedback')
    client_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    client_photo = models.URLField(max_length=350)

    job_title = models.CharField(max_length=250)
    market_place = models.CharField(max_length=150)
    contract_start = models.DateField()
    contract_end = models.DateField()
    rating = models.FloatField()
    feedback = models.TextField(max_length=350)


class ContactRequest(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_request')
    name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=350)


class PresentAddress(BaseModel):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='present_address')
    care_of = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    road_name = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    ward_no = models.CharField(max_length=200)
    post_office = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    division = models.CharField(max_length=200)


class PermanentAddress(BaseModel):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='permanent_address')
    care_of = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    road_name = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    ward_no = models.CharField(max_length=200)
    post_office = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    division = models.CharField(max_length=200)