from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Post, Category, Tag


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


       



class PostListSerialize(ModelSerializer):

    class Meta:
        model = Post
        fields = ['author', 'title', 'body']
