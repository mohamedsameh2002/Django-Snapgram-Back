from django.urls import path
from . import views
urlpatterns = [
    path('posts/',views.Posts_api.as_view(),name='post'),
    path('posts/like-dis/<uuid:post_id>/',views.like_dislike,name='lik_dis'),
    path('posts/save-cancel/',views.save_cancel,name='save_cancel'),
    path('posts/post-details/',views.PostDetails.as_view(),name='post_details'),
    path('posts/explore/',views.Explore.as_view(),name='explore'),
    path('posts/profileposts/',views.ProfilePosts.as_view(),name='profileposts'),
    path('posts/saved-posts/',views.MySavedPosts.as_view(),name='saved-posts'),
    path('posts/search/',views.Search.as_view(),name='search'),
]