from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.authtoken.models import Token

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **other_fields)

class Staff(AbstractBaseUser):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(
        verbose_name="Email Address",
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def tokens(self):
        token = Token.objects.get_or_create(user=self)
        return token[0].key

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

    
class Student(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    department = models.CharField(max_length=25)
    reg_no = models.PositiveIntegerField()


class Resource(models.Model):
    resource_id = models.CharField(max_length=35, primary_key=True)
