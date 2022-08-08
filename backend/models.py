from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, password, is_active = True, is_staff = False, is_admin = False):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email')
        if not phone:
            raise ValueError('Users must have an phone')
        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone = phone,
            password=password,
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, phone, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            phone = phone,
            password=password,
            is_staff = True, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, phone, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            phone = phone,
            password=password,
            is_staff = True, 
            is_admin = True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, phone, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            phone = phone,
            password=password,
            is_staff = True, 
            is_admin = True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone', 'password'] # Email &amp; Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active







