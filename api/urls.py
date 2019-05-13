from django.urls import path, include
from . import views

from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('blog.urls')),
]

urlpatterns += [
    path('rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/twitter/', views.TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/facebook/connect/', views.FacebookConnect.as_view(), name='fb_connect'),
    path('rest-auth/twitter/connect/', views.TwitterConnect.as_view(), name='twitter_connect'),
    path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'
    ),
    path('socialaccounts/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'
    )
]
