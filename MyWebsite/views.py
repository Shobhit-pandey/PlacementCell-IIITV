# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect

from MyWebsite.form import RecruiterForm, BeyondAcademicImagesForm, BeyondAcademicVideosForm, \
    BeyondAcademicHighlightForm
from MyWebsite.models import BeyondAcademicImages, BeyondAcademicVideos


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

def beyond_academic(request):
    image = BeyondAcademicImages.objects.all()
    video = BeyondAcademicVideos.objects.all()
    return render(request, 'beyond_academics.html',{'image':image,'video':video})

def Addimages(request):
    if request.method == 'POST':
        form = BeyondAcademicImagesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicImagesForm()
    return render(request,'AddImage.html',{'form':form})


def Addvideos(request):
    if request.method == 'POST':
        form = BeyondAcademicVideosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicVideosForm()
    return render(request,'AddVideo.html',{'form':form})


def AddHighlight(request):
    if request.method == "POST":
        form =  BeyondAcademicHighlightForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicHighlightForm()
    return render(request,'AddHighlight.html',{'form':form})

