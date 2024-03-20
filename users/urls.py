from django.urls import path
from . import views
urlpatterns = [
    path('all-users/',views.all_users,name='all-users'),
    path('create-follows/',views.create_follows,name='create-follows'),
    path('profile_data/',views.profile_data,name='profile_data'),
    path('update-user-data/',views.update_user_data,name='update-user-data'),
]