from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from blog.models import Tag
from blog.serializers.tag import TagSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes=[AllowAny]


class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    permission_classes=[AllowAny]


class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes=[AllowAny]


class TagUpdateView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    permission_classes=[AllowAny]


class TagDeleteView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
   
    permission_classes=[AllowAny]
