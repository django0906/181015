from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_of_schools, name="list_of_schools"),
    path('<int:school_id>', views.school_details, name="school_details"),
    path('<int:student_id>', views.student_details, name="student_details"),
]