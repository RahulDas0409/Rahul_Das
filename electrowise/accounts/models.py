from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class AccountsManager(BaseUserManager):
    def create_user(self, aadhaar_no, first_name, last_name, phone_no, email, role, address, city, state, pin, password, **other_fields):
        if not (email and phone_no):
            raise ValueError("User should have an email address and a phone number.")
        if not aadhaar_no:
            raise ValueError("User should have an aadhaar number.")
        if not (first_name and last_name):
            raise ValueError("User should have an full name.")
        if not role:
            raise ValueError("User should mention he/she a doctor or patient.")
        if not (address and city):
            raise ValueError("User should have a address.")
        if not state:
            raise ValueError("User should mention his/her state.")
        if not pin:
            raise ValueError("User should mention his/her PIN code.")
        
        user = self.model(
            aadhaar_no = aadhaar_no,
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            email=email,
            role=role,
            address=address,
            city=city,
            state=state,
            pin=pin,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, aadhaar_no, first_name, last_name, phone_no, email, role, address, city, state, pin, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_admin', True)
        return self.create_user(aadhaar_no, first_name, last_name, phone_no, email, role, address, city, state, pin, password, **other_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    aadhaar_no = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, default="Patient")
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    pin = models.CharField(max_length=20)

    USERNAME_FIELD = 'aadhaar_no'
    REQUIRED_FIELDS = ['first_name','last_name','phone_no','email','role','address','city','state','pin']

    objects = AccountsManager()

    def __str__(self):
        return self.first_name+' '+self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True