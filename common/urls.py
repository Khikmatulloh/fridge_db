from django.urls import path

from .views import index,SponsorListView, SponsorDetailView,SponsorCreateView, SponsorUpdateView, SponsorDeleteView

urlpatterns = [
    path("", index, name="home"),
    path("sponsors/", SponsorListView.as_view(), name="sponsor-list"),
    path("sponsors/<int:pk>/", SponsorDetailView.as_view(), name="sponsor-detail"),
    path("sponsors/create/", SponsorCreateView.as_view(), name="sponsor-create"),
    path("sponsors/update/<int:pk>/", SponsorUpdateView.as_view(), name="sponsor-update"),
    path("sponsors/delete/<int:pk>/", SponsorDeleteView.as_view(), name="sponsor-delete"),
]
