from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('tags/', TagListCreateView.as_view()),
    path('', include(router.urls))

    # path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('posts/<slug:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))

]

