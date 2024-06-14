from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from studentapp.models import Student, Course, StudentCourseProgress, Video, VideoView
from api.serializers import StudentSerializer, CourseSerializer, StudentCourseProgressSerializer, VideoSerializer, VideoViewSerializer

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentCourseProgressView(ModelViewSet):
    queryset = StudentCourseProgress.objects.all()
    serializer_class = StudentCourseProgressSerializer

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoViewViewSet(ModelViewSet):
    queryset = VideoView.objects.all()
    serializer_class = VideoViewSerializer