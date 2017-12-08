# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect

from MyWebsite.form import RecruiterForm, BeyondAcademicImagesForm, BeyondAcademicVideosForm, \
    BeyondAcademicHighlightForm, RecruiterInternshipIndustrialForm, RecruiterInternshipNGOForm, PastRecruiterForm
from MyWebsite.models import BeyondAcademicImages, BeyondAcademicVideos, BeyondAcademicsHighlight, PastRecruiter, \
    RecruiterInternshipIndustrial, RecruiterInternshipNGO


def home(request):
    return render(request,'home.html')

def student(request):
    return render(request,'Student.html')

def recruiter(request):
    images = PastRecruiter.objects.all()
    industrials = RecruiterInternshipIndustrial.objects.all()
    ngos = RecruiterInternshipNGO.objects.all()
    return render(request,'Recruiter.html',{'images':images,'industrials':industrials,'ngos':ngos})

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
    highlight = BeyondAcademicsHighlight.objects.all()
    return render(request, 'beyond_academics.html',{'image':image,'video':video,'highlight':highlight})

def AddBeyondAcademicimages(request):
    if request.method == 'POST':
        form = BeyondAcademicImagesForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicImagesForm()
    return render(request, 'AddBeyondAcademicImage.html', {'form':form})


def AddBeyondAcademicvideos(request):
    if request.method == 'POST':
        form = BeyondAcademicVideosForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicVideosForm()
    return render(request, 'AddBeyondAcademicVideo.html', {'form':form})


def AddBeyondAcademicHighlight(request):
    if request.method == "POST":
        form =  BeyondAcademicHighlightForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicHighlightForm()
    return render(request, 'AddBeyondAcademicHighlight.html', {'form':form})




def Addinterndescrip(request):
    if request.method == 'POST':
        form =RecruiterInternshipIndustrialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:recruiter')

    else:
        form = RecruiterInternshipIndustrialForm()
    return render(request,'AddRecruiterInternshipIndustrial.html',{'form':form})


def Addngodescrip(request):
    if request.method == 'POST':
        form =RecruiterInternshipNGOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:recruiter')

    else:
        form = RecruiterInternshipNGOForm()
    return render(request,'AddRecruiterInternshipNGO.html',{'form':form})


def addPastRecruiterimage(request):
    if request.method == 'POST':
        form =PastRecruiterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:recruiter')

    else:
        form = PastRecruiterForm()
    return render(request,'Addpastrecuiter.html',{'form':form})
