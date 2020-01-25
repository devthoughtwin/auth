from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from datetime import datetime, date, timedelta
# from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class BaseModel(models.Model):
    # Timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class UserManager(BaseUserManager):
    """ Well.. using BaseUserManager """
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must register an email")

        user = self.model(email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user

""" User Account Model """
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # first_name = models.CharField(max_length=140,null=True, blank=True)
    # last_name = models.CharField(max_length=140,null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.profile.full_name


    @property
    def username(self):
        return self.email

    @property
    def profile(self):
        return self.user_profile.all()[0]

    def get_services_count(self):
        return self.user_services.all().count()

class UserProfile(BaseModel):
    user = models.ForeignKey(User,related_name='user_profile', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    mobile_number = models.CharField(max_length=140)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=140,null=True, blank=True)
    state = models.CharField(max_length=140,null=True, blank=True)
    zip_code = models.CharField(max_length=140,null=True, blank=True)
    profile_pic = models.FileField(upload_to='profile/', null=True, blank=True)
    company_name = models.CharField("Company Name",max_length=500,null=True, blank=True)

    @property
    def full_name(self):
        return self.user.first_name and "%s %s"%(self.user.first_name, self.user.last_name) or self.user.email

    def __str__(self):
        return self.user.email

    # def get_absolute_url(self):

    #     return reverse('users:user-profile-update' ,kwargs={'pk':self.pk})

    # def wallet_balance(self):
    #     total_credited = sum([w.balance for w in self.user.wallets.filter(type='1')])
    #     total_debited = sum([w.balance for w in self.user.wallets.filter(type='2')])
    #     return total_credited - total_debited

    # def total_earn(self):
    #     return sum([w.balance for w in self.user.wallets.filter(type='2')])

# """Use when send email on create user and contact form submition"""
# def send_email( subject, text_content, html_content):
#     from_email='alert@plumdry.com'
#     to_email=['support@plumdry.com']
#     msg = EmailMultiAlternatives(subject, text_content, from_email,to_email)
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()

# def send_user_created_email(user_obj):
#     subject = "New User Added in plumdry"
#     text_content = render_to_string('email/users/user_create.txt',{'user' : user_obj})
#     html_content = render_to_string('email/users/user_create.html',{'user' : user_obj})
#     send_email( subject, text_content, html_content)

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
        # Token.objects.get_or_create(user=instance)
        # send_user_created_email(instance)