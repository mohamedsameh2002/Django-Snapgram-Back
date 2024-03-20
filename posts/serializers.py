from .models import *
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','username','Bio','email','image']




class PostSerializer(serializers.ModelSerializer):
    # form_name=serializers.CharField(source="publisher.name",required=False)
    fans=UserSerializer(many=True,required=False)
    publisher=UserSerializer(many=False,required=False)
    class Meta():
        model = Post
        fields = [ 'id','caption', 'file','fans', 'location', 'publisher','created_at']


class SavedPostsSerializer(serializers.ModelSerializer):
    # form_name=serializers.CharField(source="publisher.name",required=False)
    post=PostSerializer(many=False)
    class Meta():
        model = SavedPosts
        fields = [ 'post',]
