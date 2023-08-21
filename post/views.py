from rest_framework import generics, viewsets, filters
from .models import Post, Category, Tag
from .serializers import PostDetailSerializer, PostListSerialize, CategorySerializer, TagSerializer
import django_filters



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    

# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
    
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return PostListSerialize
#         return PostDetailSerializer


# class PostRetriveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tags__slug', 'category', 'author']
    search_fields = ['title', 'body'] 
    ordering_fields = ['created_at', 'title']   

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerialize
        return PostDetailSerializer
        
