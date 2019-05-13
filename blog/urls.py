from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('blog/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('blog/', views.BlogPost.as_view(), name='post-list'),
    path('draft/', views.MyPosts.as_view(), name='draft'),

    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)