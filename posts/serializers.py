from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.Field(source='owner.username')
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'createAt', 'owner', 'published']
        read_only_fields = ('owner',)
