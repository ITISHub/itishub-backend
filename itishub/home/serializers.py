from rest_framework import serializers

from .models import *

class HomeCardListSerializer(serializers.ModelSerializer):
    '''Serializer for HomeCard'''

    class Meta:
        model = HomeCard
        fields = "__all__"


class CreatorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = "__all__"

class UsefulLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsefulLink
        fields = ('url','title')

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"

    useful_links = UsefulLinkSerializer(many=True)


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    lessons = LessonSerializer(source='get_lessons', many=True)

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    lessons = LessonSerializer(source='get_lessons', many=True)


