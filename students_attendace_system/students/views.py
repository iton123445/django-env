from django.http import HttpResponse
from django.template import loader
from . models import Students
from django.shortcuts import render
from .forms import StudentForm

def  students(request):
    students= Students.objects.all().values()
    template = loader.get_template('students_list.html')
    context = {
        'students_list': students,
    }
    return HttpResponse(template.render(context, request))


def  details(request,id):
    students= Students.objects.get(id=id)
    template = loader.get_template('students_details.html')
    context = {
        'students_list': students,
    }
    return HttpResponse(template.render(context, request))

def  main(request):
     template = loader.get_template('main.html')
     return HttpResponse(template.render())


