from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering=["email"]
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=User
    list_display=["email","name","username","is_active","is_staff"]
    list_display_links=["email"]
    list_filter=["email","name","username","is_active","is_staff"]
    search_fields=["emali","name","username"]
    fieldsets = (
        (
            _("Login Credentials"), {
                "fields": ("email", "password",)
            }, 
        ),
        (
            _("Personal Information"),
            {
                "fields": ('name','username','image','Bio','followers')
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": ("email", "name" ,'username',"password1", "password2", "is_staff", "is_active"),
            },),
        )


admin.site.register(User,UserAdmin)