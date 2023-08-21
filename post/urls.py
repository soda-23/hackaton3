from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostListCreateView.as_view()), 
    path('posts/<slug:pk>/', PostRetriveView.as_view()),
    path('categories/', CategoryListCreateView.as_view()),
    path('tags/', TagListCreateView.as_view())

]

