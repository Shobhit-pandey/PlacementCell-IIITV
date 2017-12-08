# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request,'home.html')

def student(request):
    return render(request,'Student.html')

def recruiter(request):
    return render(request,'Recruiter.html')

def about(request):
    return render(request,'About.html')

def procedure(request):
    return render(request, 'Procedure.html')

def academic(request):
    return render(request, 'Academic.html')

def contact(request) :
    return render(request, 'Contact.html')
def department(request):
    return render(request, 'departments.html')

def beyondacademics(request):
    return render(request, 'beyond.html')


