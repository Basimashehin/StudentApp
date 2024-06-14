from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Course, StudentCourseProgress, Video, VideoView

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourseProgress)
admin.site.register(Video)
admin.site.register(VideoView)
