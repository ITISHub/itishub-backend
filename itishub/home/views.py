from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeCard,Creator,Course,Lesson
from .serializers import *

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

class CourseListView(APIView):

    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseListSerializer(courses,many=True)
        return Response(serializer.data)

class LessonView(APIView):

    def get(self, request, pk):
        lesson = Lesson.objects.get(id=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)


class CourseView(APIView):

    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)