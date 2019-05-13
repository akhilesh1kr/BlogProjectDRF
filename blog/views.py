from django.contrib.auth.models import User

from rest_framework import generics, permissions, renderers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Post
from .permissions import IsOwnerOrReadOnly
from api.serializers import PostSerializer, PostDetailSerializer, MyPostSerializer, UserSerializer

from django.db.models import Q

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'Users': reverse('user-list', request=request, format=format),
        'Blog': reverse('post-list', request=request, format=format),
        'My Posts': reverse('draft', request=request, format=format)
    })

class BlogPost(generics.ListAPIView):
    queryset = Post.objects.filter(publish=True)
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(Q(author=self.request.user) | Q(publish=True))
        return Post.objects.filter(publish=True)


class MyPosts(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(author=request.user)
    serializer_class = MyPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer