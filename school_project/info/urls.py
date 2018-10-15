from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_of_schools, name="list_of_schools"),
    path('school/<int:info_school.id>', views.school_details, name="school_details"),
    path('student_list', views.list_of_students, name="list_of_students"),
    path('student/<int:student.id>', views.student_details, name="student_details"),
]