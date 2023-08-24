from rest_framework import generics, viewsets, filters
from .models import Post, Category, Tag
from .serializers import PostDetailSerializer, PostListSerialize, CategorySerializer, TagSerializer
import django_filters
from rest_framework.permissions import AllowAny
from .permissions import IsAuthorPermission, IsAdminOrIsAuthenticatedPermission
from rest_framework.decorators import action
from review.serializers import RatingSerializer
from review.models import Rating
from rest_framework.response import Response


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
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    filterset_fields = ['tags__slug', 'category', 'author']
    search_fields = ['title', 'body'] 
    ordering_fields = ['created_at', 'title']   

    @action(methods=['POST', 'PATCH'], detail=True)
    def set_rating(self, request, pk=None):
        # data = request.data
        data = request.data.copy()
        data['post'] = pk
        serializer = RatingSerializer(data=data, context = {'request': request})
        rating = Rating.objects.filter(
            author=request.user, 
            post=pk
        ).first()

        # print('============')
        # print(rating)
        # print('============')
        if serializer.is_valid(raise_exception=True):
            if rating and request.method == 'POST':
                return Response(
                    'Rating object exists', status=200
                )
            elif rating and request.method == 'PATCH':
                serializer.update(rating, serializer.validated_data)
                return Response(
                    serializer.data, status=200
                )
            elif request.method == 'POST':
                serializer.create(serializer.validated_data)
                return Response(serializer.data, status=201)




    def get_serializer_class(self):
    
        if self.action == 'list':
            return PostListSerialize
        return PostDetailSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminOrIsAuthenticatedPermission]

        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

        

        
