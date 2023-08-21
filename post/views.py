from rest_framework import generics
from .models import Post, Category, Tag
from .serializers import PostDetailSerializer, PostListSerialize, CategorySerializer, TagSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerialize
        return PostDetailSerializer


class PostRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer





