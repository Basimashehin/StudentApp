# Create your models here.
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.student_name

class StudentCourseProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    expected_completion_date = models.DateField()
    actual_completion_date = models.DateField()

    def __str__(self):
        return f"{self.student.student_name} - {self.course.course_name}"

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class VideoView(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.video.title} view at {self.timestamp}"




