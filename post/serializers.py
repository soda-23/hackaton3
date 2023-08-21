from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Post, Category, Tag


class ValidationMixin:
    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise ValidationError(
                'такое название уже существует'               
            )
        return title



class CategorySerializer(ValidationMixin, ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(ValidationMixin, ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title',)



class PostDetailSerializer(ValidationMixin, ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerialize(ValidationMixin, ModelSerializer):

    class Meta:
        model = Post
        fields = ['author', 'title', 'body']
