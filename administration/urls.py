from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name="administration"),
    path('courses/', views.course_admin, name="course_admin"),
    path('courses/<int:pk>', views.edit_course, name="edit_course"),
]