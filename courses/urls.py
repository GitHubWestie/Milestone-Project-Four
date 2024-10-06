from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_courses, name="get_courses"),
    path('lesson/<uuid:uuid>/', views.get_lesson, name="get_lesson"),
]