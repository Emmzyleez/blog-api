
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        
        fields = ('url','id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username')
