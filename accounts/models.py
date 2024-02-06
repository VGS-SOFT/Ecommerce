from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password


def send_account_activation_email(email , email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject , message , email_from , [email])
    
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        abstract = True

class CustomUserManager(BaseUserManager):
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        
    def create_user(self, email, password=None, mobilenumber=None, **extra_fields):
        if not email and not mobilenumber:
            raise ValueError('Either Email or Mobile Number must be set')

        email = self.normalize_email(email) if email else None
        username = email.split('@')[0] if email else None
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, mobilenumber=mobilenumber,
                          username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, mobilenumber=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, mobilenumber, **extra_fields)

    def authenticate(self, request, email=None, mobilenumber=None, password=None, **extra_fields):
        UserModel = get_user_model()

        # if email:
        #     user = UserModel.objects.filter(email=email).first()
        # elif mobilenumber:
        #     user = UserModel.objects.filter(mobilenumber=mobilenumber).first()
        # else:
        #     return None  # No email or mobile number provided

        # if user and user.check_password(password):
        #     return user

        # return None
        if email:
            user = UserModel.objects.filter(email=email).first()
        elif mobilenumber:
            user = UserModel.objects.filter(mobilenumber=mobilenumber).first()
        else:
            return None  # No email or mobile number provided

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)
    mobilenumber = models.CharField(max_length=15, blank=True, null=True, unique=True)
    profilepitcure = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    isdeleted = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    createdby = models.IntegerField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    resetcode = models.TextField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(
        max_length=150, unique=True, blank=True, null=True)

    objects = CustomUserManager()

    # Update related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group, related_name='custom_user_set', blank=True, help_text='The groups this user belongs to.')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_set', blank=True, help_text='Specific permissions for this user.')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobilenumber']

    def __str__(self):
        return self.email or self.mobilenumber

class Profile(BaseModel):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    profile_image = models.ImageField(upload_to = 'profile')


@receiver(post_save , sender = CustomUser)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)