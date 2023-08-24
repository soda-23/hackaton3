from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Comment, Like, Rating


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create( author=user, **validated_data)
        return comment        

    class Meta:
        model = Comment
        fields = '__all__'




