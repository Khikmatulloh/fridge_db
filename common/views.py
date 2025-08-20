from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from common.models import Sponsor
from common.serializers.sponsor import SponsorSerializer

def index(request):
    return render(request, "index.html")
class SponsorListView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDetailView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_field = "pk"


class SponsorCreateView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorUpdateView(UpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_field = "pk"


class SponsorDeleteView(DestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_field = "pk"
