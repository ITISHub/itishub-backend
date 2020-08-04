from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeCard
from .serializers import HomeCardListSerializer

# Create your views here.

class HomeCardListView(APIView):

    def get(self,request):
        homeCards = HomeCard.objects.all()
        serializer = HomeCardListSerializer(homeCards,many=True)
        return Response(serializer.data)
