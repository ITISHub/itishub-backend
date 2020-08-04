from rest_framework import serializers

from .models import HomeCard,Creator

class HomeCardListSerializer(serializers.ModelSerializer):
    '''Serializer for HomeCard'''

    class Meta:
        model = HomeCard
        fields = "__all__"


class CreatorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = "__all__"
