from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .models import School, Students


def list_of_schools(request):
    '''
    모든 학교 목록을 출력.
    학교 상세보기 링크 구현
    :param request:
    :return:
    '''
    school_list = School.objects.all()

    template = get_template('info/info_of_schools.html')
    context = {'list_of_schools': school_list}
    return HttpResponse(template.render(context, request))


def school_details(request):
    '''
    학교 상세보기
        URL 이름으로 school_id를 사용, 해당 학교 출력.
        속하는 모든 학생 목록을 보여줌.
        학생 상세보기 링크 구현
    :param request:
    :return:
    '''
    print("aaaa")
    school_detail = School.objects.get(id=School.school_name)

    template = get_template('info/school_details.html')
    context = {}
    return HttpResponse(template.render(context, request))


def list_of_students(request):
    student_list = Students.objects.all()

    template = get_template('info/list_of_students.html')

    context = {'list_of_students': student_list}
    return HttpResponse(template.render(context, request))


def student_details(request):
    template = get_template('info/student_details.html')

    context = {}
    return HttpResponse(template.render(context, request))

