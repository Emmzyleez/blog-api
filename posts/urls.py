
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, PostList, PostDetail, api_root  

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'), 
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)






