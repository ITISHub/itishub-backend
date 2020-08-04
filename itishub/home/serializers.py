from rest_framework import serializers

from .models import HomeCard

class HomeCardListSerializer(serializers.ModelSerializer):
    '''Serializer for HomeCard'''

    class Meta:
        model = HomeCard
        fields = ('title','image','url')
