from rest_framework import serializers
from blog.models import BlogPost, Comment


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "slug", "status", "published_at", "user", "category"]
