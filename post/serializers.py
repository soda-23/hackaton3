from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Post, Category, Tag
from django.db.models import Avg
from review.serializers import CommentSerializer
from review.models import Comment


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title', 'slug')



class PostDetailSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(author=user, **validated_data)
        post.tags.add(*tags)
        return post
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        representation['commets'] = CommentSerializer(Comment.objects.filter(post=instance.pk), many=True).data
        return representation
    


       



class PostListSerialize(ModelSerializer):

    class Meta:
        model = Post
        fields = ['author', 'title', 'body']


