# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def student(request):
    return render(request,'Student.html')

def recruiter(request):
    return render(request,'Recruiter.html')

def about(request):
    return render(request,'About.html')

def procedure(request):
    return render(request,'Procedure.html')