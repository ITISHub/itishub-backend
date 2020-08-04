from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeCard,Creator
from .serializers import HomeCardListSerializer,CreatorListSerializer

# Create your views here.

class HomeCardListView(APIView):

    def get(self,request):
        homeCards = HomeCard.objects.all()
        serializer = HomeCardListSerializer(homeCards,many=True)
        return Response(serializer.data)

class CreatorListView(APIView):

    def get(self,request):
        creators = Creator.objects.all()
        serializer = CreatorListSerializer(creators,many=True)
        return Response(serializer.data)

