# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from MyWebsite.form import RecruiterForm


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

def academic(request):
    return render(request,'Academic.html')

def contact(request):
    return render(request,'Contact.html')
def department(request):
    return render(request,'departments.html')
def recruiter_form(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:home')
    else:
        form = RecruiterForm()
    return render(request, 'recruiterform.html', {'form': form})
