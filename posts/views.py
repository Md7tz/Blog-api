from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# read/write => ListCreateAPIView
class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# read/write/delete => RetrieveUpdateDestroyAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
