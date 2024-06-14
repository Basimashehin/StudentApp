from rest_framework import serializers
from studentapp.models import Course, Student, StudentCourseProgress, Video, VideoView

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentCourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseProgress
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class VideoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoView
        fields = "__all__"


