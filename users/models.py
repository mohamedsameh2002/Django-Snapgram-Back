from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.



class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(_("Name"),max_length=15)
    username=models.CharField(_("Username"),max_length=10,unique=True)
    email=models.EmailField(_("Email Address"),max_length=200,unique=True)
    image=models.ImageField(upload_to='users_images/',null=True,blank=True)
    Bio=models.CharField(max_length=100,null=True,blank=True)
    followers=models.ManyToManyField('User',null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    data_joined=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=["name",'email']
    objects=CustomUserManager()

    class Meta:
        verbose_name=_("User")
        verbose_name_plural=_("Users")
    def __str__(self):
        return self.username
    
    