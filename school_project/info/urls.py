from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [
    path('', views.list_of_schools, name="list_of_schools"),
    path('school/<int:school_id>/', views.school_details, name="school_details"),
    path('student/', views.list_of_students, name="list_of_students"),
    path('student/<int:student_id>/', views.student_details, name="student_details"),
]