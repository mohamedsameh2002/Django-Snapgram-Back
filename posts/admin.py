from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin (admin.ModelAdmin):
    list_display=['created_at','publisher']
admin.site.register(Post,PostAdmin)
admin.site.register(SavedPosts)