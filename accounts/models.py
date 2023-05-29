from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, name, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, name, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=255, default="John")
    email = models.EmailField(_('email address'), unique=True)
    linked_companies = models.ManyToManyField("Company", through="UserCompanyRelation")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
# Company model
class Company(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    category = models.ManyToManyField("Category")
    stage = models.ManyToManyField("Stage")
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_of_creation = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class UserCompanyRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)