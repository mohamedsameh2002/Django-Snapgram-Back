from rest_framework.decorators import api_view,permission_classes
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets,generics
from rest_framework.permissions import IsAuthenticated
from .pagination import MyPageNumberPagination
from django.db.models import Q

# Create your views here.


class Posts_api (APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(publisher=request.user)
            return Response( status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_dislike(request,post_id):
    user=request.user
    post=Post.objects.get(id=post_id)
    if post.fans.filter(username=user.username).exists():
        post.fans.remove(user)
    else:
        post.fans.add(user)
        post.save()
    return Response( status=status.HTTP_202_ACCEPTED)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def save_cancel(request):
    user=request.user
    if request.method == 'POST':
        post=Post.objects.get(id=request.data['post_id'])
        try:
            post_save=SavedPosts.objects.get(user=user,post__id=request.data['post_id'])
            post_save.delete()
        except SavedPosts.DoesNotExist:
            SavedPosts.objects.create(user=user,post=post)
        return Response( status=status.HTTP_202_ACCEPTED)
    else:
        user_saved_posts=SavedPosts.objects.filter(user=user)
        serializer=SavedPostsSerializer(user_saved_posts,many=True)
        return Response( data=serializer.data,status=status.HTTP_200_OK)


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def post_details(request):
#     post=get_object_or_404(Post,id=request.data['post_id'])
#     serializer=SavedPostsSerializer(post,many=False)
#     return Response( data=serializer.data,status=status.HTTP_200_OK)
    



class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes=[IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        post_id=self.request.query_params['post_id']
        post=Post.objects.get(id=post_id)
        serializer=PostSerializer(post,many=False)
        return Response(serializer.data)
    

    def update(self, request, *args, **kwargs):
        post=Post.objects.get(id=request.data['post_id'])
        serializer=PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        Post.objects.get(id=request.data['post_id']).delete()
        return Response(status=status.HTTP_200_OK)

class Explore (generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    pagination_class=MyPageNumberPagination
    serializer_class=PostSerializer
    queryset=Post.objects.all()



class ProfilePosts(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = MyPageNumberPagination  
    serializer_class = PostSerializer
    def get_queryset(self):
        username = self.request.query_params['username']
        return Post.objects.filter(publisher__username=username)
    

class MySavedPosts(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = MyPageNumberPagination  
    serializer_class = SavedPostsSerializer
    def get_queryset(self):
        return SavedPosts.objects.filter(user=self.request.user)
    

class Search(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    pagination_class=MyPageNumberPagination
    serializer_class=PostSerializer
    def get_queryset(self):
        return Post.objects.filter(
            Q(publisher__username__icontains=self.request.query_params['q'])|
            Q(caption__icontains=self.request.query_params['q'])|
            Q(publisher__name__icontains=self.request.query_params['q'])
            )


