from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager (BaseUserManager):
    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))
        
    def create_user(self,name,username,email,password,*args, **kwargs):
        if not name:
            raise ValueError(_("User must submit a name"))
        if not username:
            raise ValueError(_("User must submit a username"))
        if  email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User: and email address is required"))
        user=self.model(
            name=name,
            email=email,
            username=username,
            **kwargs
        )
        user.set_password(password)
        kwargs.setdefault('is_staff',False)
        kwargs.setdefault('is_superuser',False)
        kwargs.setdefault('is_active',False)
        user.save()
        return user
    
    def create_superuser(self,username,name,email,password,*args, **kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        if kwargs.get('is_staff') is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        if not password:
            raise ValueError(_("Superuser must have a password"))
        if  email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin User: and email address is required"))
        
        user=self.create_user(name,username,email,password,*args, **kwargs)
        user.save()
        return user
