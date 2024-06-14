from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentView, CourseView, StudentCourseProgressView, VideoViewSet, VideoViewViewSet
router = DefaultRouter()
router.register(r'students', StudentView, basename="student")
router.register(r'courses', CourseView, basename="course")
router.register(r'studentsprogress', StudentCourseProgressView, basename="studentprogress")
router.register(r'video', VideoViewSet, basename="video")
router.register(r'videoview', VideoViewViewSet, basename="videoview")

urlpatterns = [
    path('', include(router.urls))
]
