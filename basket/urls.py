from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_basket, name="view_basket"),
    path('add/<int:course_id>', views.add_to_basket, name="add_to_basket"),
    path('remove/<int:course_id>', views.remove_from_basket,
         name="remove_from_basket")
]
