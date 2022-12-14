# Generated by Django 4.1.1 on 2022-10-24 16:27

from django.db import migrations, models
import userinfo.models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_rename_user_id_permanentaddress_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientfeedback',
            name='client_photo',
            field=models.ImageField(help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='client_img/', validators=[userinfo.models.file_size]),
        ),
        migrations.AlterField(
            model_name='experince',
            name='company_logo',
            field=models.ImageField(help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='company_logo/', validators=[userinfo.models.file_size]),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_img',
            field=models.ImageField(help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='project_cover/', validators=[userinfo.models.file_size]),
        ),
        migrations.AlterField(
            model_name='portfolioinfo',
            name='banner_image',
            field=models.ImageField(help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='banner_img/', validators=[userinfo.models.file_size]),
        ),
        migrations.AlterField(
            model_name='portfolioinfo',
            name='footer_image',
            field=models.ImageField(help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='footer_img/', validators=[userinfo.models.file_size]),
        ),
        migrations.AlterField(
            model_name='portfolioinfo',
            name='profile_img',
            field=models.ImageField(default='profile_img/default.jpg', help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='profile_img/', validators=[userinfo.models.file_size]),
        ),
        migrations.AlterField(
            model_name='professionalskills',
            name='skill_logo',
            field=models.ImageField(help_text='File size should be less than 1mb(.jpg/.png/.gif)', upload_to='skill_logo/', validators=[userinfo.models.file_size]),
        ),
    ]
