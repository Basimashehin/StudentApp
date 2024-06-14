from django.shortcuts import render
from .models import Student, Course, StudentCourseProgress, Video, VideoView
from django.db.models import Count
from django.db.models.functions import ExtractDay,ExtractWeek

def detail(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    context = {
        'student': students,
        'course': courses,
    }
    return render(request, 'detailview.html', context)

def categorize_videos(videos):
    threshold = 10  # Define your threshold for least and most watched
    categorized_videos = {
        'least_watched': [],
        'most_watched': []
    }

    for video in videos:
        if video.views < threshold:
            categorized_videos['least_watched'].append(video)
        else:
            categorized_videos['most_watched'].append(video)

    return categorized_videos


def calculate_peak_timing(video):
    views = VideoView.objects.filter(video=video)
    day_count = views.annotate(day=ExtractDay('timestamp')).values('day').annotate(count=Count('id')).order_by('-count')
    week_count = views.annotate(week=ExtractWeek('timestamp')).values('week').annotate(count=Count('id')).order_by('-count')
    if day_count:
        peak_day = day_count[0]['day']
    else:
        peak_day = "No views"

    if week_count:
        peak_week = week_count[0]['week']
    else:
        peak_week = "No views"

    return {'peak_day': peak_day, 'peak_week': peak_week}


def categorize_data(progress):
    categorized_data = {
        'exceeded_expectations': [],
        'as_per_expectation': [],
        'below_expectations': []
    }
    for p in progress:
        if p.actual_completion_date < p.expected_completion_date:
            categorized_data['exceeded_expectations'].append(p)
        elif p.actual_completion_date == p.expected_completion_date:
            categorized_data['as_per_expectation'].append(p)
        else:
            categorized_data['below_expectations'].append(p)

    return categorized_data

def dashboard(request):
    progress = StudentCourseProgress.objects.all()
    videos = Video.objects.all()
    categorized_videos = categorize_videos(videos)
    categorized_data = categorize_data(progress)
    video_peak_timings = {}
    for video in videos:
        video_peak_timings[video.title] = calculate_peak_timing(video)

    context = {
        'progress': progress,
        'videos': videos,
        'categorized_data': categorized_data,
        'categorized_videos': categorized_videos,
        'video_peak_timings': video_peak_timings,
    }
    return render(request, 'dashboard.html', context)

# video_peak_timings = {'python introduction': {'peak_day': 12, 'peak_week': 24},
#                       'datatypes in python': {'peak_day': 12, 'peak_week': 24}}
