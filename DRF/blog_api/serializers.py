from rest_framework import serializers
from blog.models import Post
from django.conf import settings

# Serializers allow complex data such as querysets and model instances to 
# be converted to native Python datatypes that can then be easily rendered 
# into JSON, XML or other content types

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug','author', 'excerpt', 'content', 'status')

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}