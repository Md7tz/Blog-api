from rest_framework import generics, permissions # , permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


# read/write => ListCreateAPIView
class PostList(generics.ListCreateAPIView):
  # permission_classes = (permissions.IsAuthenticated,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# read/write/delete => RetrieveUpdateDestroyAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (permissions.IsAuthenticated,)
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer
