from django.urls import path
from .views import home_view, about_view, course_view, teacher_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('course/', course_view, name='course'),
    path('teacher/', teacher_view, name='teacher'),
]