from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    require_mfa = models.BooleanField(default=False)
    tfa_secret = models.CharField(max_length=255, default='')
    usfa_membership = models.IntegerField(null=True, blank=True)
    user_handle = models.CharField(max_length=25, null=True, blank=True, unique=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# Used to store JWTs
class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


# Reset email model
class Reset(models.Model):
  email = models.CharField(max_length=255)
  token = models.CharField(max_length=255, unique=True)


# blocks bad ip addresses
class BlockList(models.Model):
  ip_addr = models.CharField(max_length=10)
