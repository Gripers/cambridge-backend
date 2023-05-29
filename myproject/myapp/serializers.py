from rest_framework import serializers
from .models import Course, Teacher, Request


class TeacherSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Teacher
        depth = 1
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Request
        depth = 1
        fields = "__all__"
