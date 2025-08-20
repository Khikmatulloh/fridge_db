from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from blog.models import BlogCategory
from blog.serializers.category import BlogCategorySerializer


class BlogCategoryListView(ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogCategoryDetailView(RetrieveAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    lookup_field = "pk"


class BlogCategoryCreateView(CreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogCategoryUpdateView(UpdateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    lookup_field = "pk"


class BlogCategoryDeleteView(DestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    lookup_field = "pk"
