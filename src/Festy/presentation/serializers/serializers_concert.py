from rest_framework import serializers
from Festy.metier.model.models import Concert

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = "__all__"
        