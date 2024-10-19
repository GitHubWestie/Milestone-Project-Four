from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name="administration"),
    path('courses/', views.course_admin, name="course_admin"),
    path('courses/add', views.add_course, name="add_course"),
    path('courses/edit/<int:pk>', views.edit_course, name="edit_course"),
    path('courses/delete/<int:pk>', views.delete_course, name="delete_course"),
]