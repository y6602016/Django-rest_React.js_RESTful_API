from rest_framework import serializers
from blog.models import Post

# Serializers allow complex data such as querysets and model instances to 
# be converted to native Python datatypes that can then be easily rendered 
# into JSON, XML or other content types

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
