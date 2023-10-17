from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Custom user manager...
<<<<<<< HEAD

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,password2=None):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))
=======
class UserManager(BaseUserManager):

    def create_user(self, email,name, password=None,password2=None):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email),name=name)
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
        user.set_password(password)
        user.save(using=self._db)
        return user

<<<<<<< HEAD
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
=======

    def create_superuser(self, email,name,password,password2):
        """creates and save a new super User"""
        user = self.create_user(email=email, password=password,name=name)
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
        user.is_admin = True
        user.save(using=self._db)
        return user


<<<<<<< HEAD
=======

>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
class User(AbstractBaseUser):
    """custom user model that supports using email instead of username"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.BigIntegerField(blank=True,null=True)
    otp = models.CharField(max_length=6,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'

<<<<<<< HEAD
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin






=======

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True 

    @property  
    def is_staff(self):
        "Is the user a admin member?"
        return self.is_admin
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
