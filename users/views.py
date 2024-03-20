from rest_framework.decorators import api_view,permission_classes
from .models import *
from posts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets,generics
from rest_framework.permissions import IsAuthenticated
from .models import User
from posts.models import Post

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_users(request):
    users=User.objects.exclude(username=request.user.username).order_by('-data_joined')
    serializer=UserSerializer(users,many=True)
    return Response( data=serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_follows(request):
    user=request.user
    the_account=User.objects.get(username=request.data['username'])
    if the_account.followers.filter(username=user.username).exists():
        the_account.followers.remove(user)
    else:
        the_account.followers.add(user)
        the_account.save()
    return Response(status=status.HTTP_200_OK )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_data(request):
    user=User.objects.get(username=request.query_params['username'])
    following=User.objects.filter(followers__username__icontains=user.username)
    followers_seri=UserSerializer(user.followers,many=True)
    following_seri=UserSerializer(following,many=True)
    user_seri=UserSerializer(user,many=False)
    posts_conunt=Post.objects.filter(publisher=user).count()
    data={
        'followers':followers_seri.data,
        'following':following_seri.data,
        'posts_count':posts_conunt,
        'data':user_seri.data}
    return Response(data=data,status=status.HTTP_200_OK )

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_data(request):
    serializer=UserSerializer(request.user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK )
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST )
    


