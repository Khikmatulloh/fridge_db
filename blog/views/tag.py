from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from blog.models import Tag
from blog.serializers.tag import TagSerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"


class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"


class TagDeleteView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"
