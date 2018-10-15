from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .models import School, Students


def list_of_schools(request):
    school_list = School.objects.all

    template = get_template('info/info_of_schools.html')
    context = {'list_of_schools': school_list}
    return HttpResponse(template.render(context, request))


def school_details(request):
    template = get_template('info/school_details.html')
    pass


def list_of_students(request):
    template = get_template('info/list_of_students.html')
    pass


def student_details(request):
    template = get_template('info/student_details.html')
    pass
