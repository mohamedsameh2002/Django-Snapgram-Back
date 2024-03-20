from django.db import models
from users.models import User
# from PIL import Image
import uuid
from django.core.validators import FileExtensionValidator

# Create your models here.




class Post (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publisher=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.TextField(max_length=2200)
    file=models.FileField(upload_to='posts_files',null=True,blank=True,
                        validators=[FileExtensionValidator(allowed_extensions=['mp4','jpg','png','svg'])])
    fans=models.ManyToManyField(User,related_name='fans',null=True,blank=True)
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.location
    

class SavedPosts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    