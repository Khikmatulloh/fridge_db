from rest_framework import serializers
from common.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id", "name", "logo"]
