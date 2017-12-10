# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView

from MyWebsite.form import RecruiterForm, BeyondAcademicImagesForm, BeyondAcademicVideosForm, \
    BeyondAcademicHighlightForm, RecruiterInternshipIndustrialForm, RecruiterInternshipNGOForm, PastRecruiterForm, \
    CompaniesAppliedByStudentsForm, AlumniForm, ResearchForm, CollegeTeamImageForm, CollegeTeamFacultyForm, \
    CollegeTeamStudentForm, AcademicImageForm, AcademicVideoForm, AcademicHighlightForm
from MyWebsite.models import BeyondAcademicImages, BeyondAcademicVideos, BeyondAcademicsHighlight, PastRecruiter, \
    RecruiterInternshipIndustrial, RecruiterInternshipNGO, Recruiter, CollegeTeamImage, CollegeTeamFaculty, \
    CollegeTeamStudent, Alumni, Research, AcademicImage, AcademicVideo, AcademicHighlight
from quiz.models import Quiz


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
    addacademicimage = AcademicImage.objects.all()
    addacademicvideo = AcademicVideo.objects.all()
    addacademichighlight = AcademicHighlight.objects.all()
    return render(request,'Academic.html',{'addacademicimage':addacademicimage,'addacademicvideo':addacademicvideo,'addacademichighlight':addacademichighlight})

def college_team(request):
    addteamimage = CollegeTeamImage.objects.all()
    addfacultyimage = CollegeTeamFaculty.objects.all()
    addstudentimage = CollegeTeamStudent.objects.all()

    return render(request, 'college_team.html',{'addteamimage':addteamimage,'addfacultyimage':addfacultyimage,'addstudentimage':addstudentimage})

def contact(request):
    return render(request,'Contact.html')
def department(request):
    return render(request,'departments.html')
def alumni(request):
    alumnis = Alumni.objects.all()
    return render(request,'alumni.html',{'alumnis':alumnis})
def research_development(request):
    researchs = Research.objects.all()
    return render(request,'research_development.html',{'researchs':researchs})

@csrf_protect
def recruiter_form(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            value=form.save()
            email = form.cleaned_data['email']
            contact = form.cleaned_data['Contact_Number']
            name = form.cleaned_data['Name']
            value.save()
            email = EmailMessage('Regarding recruitment',
                                 "Received mail from"+str(email)+"\n\n"+"name:"+
                                  str(name)+"\n"+"contact:"+str(contact),to=['',])
            email.send()
            email = EmailMessage('Regarding recruitment',
                                 "Hey " + str(
                                     name) + ",\n\n" + "We have "
                                                          "recieved "
                                                          "your request "
                                                          "for recruitmrnt "
                                                          "we wiill process\n" +
                                 "We will contact you shortly on " +
                                 str(contact),
                                 to=[email,
                                     'anjansrivathsav1997@gmail.com'],
                                 reply_to=[email, ])
            email.send()
            print("reached")
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



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST , user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect("mywebsite:recruiter")
        else:
            return redirect("mywebsite:recruiter")
    else:
        form = PasswordChangeForm(user = request.user)

        args = {'form':form}

        return render(request,'change_password.html',{'form':form})

def RecruiterListView(request):
    recruiter_list = Recruiter.objects.all()
    print(recruiter_list)
    return render(request,'recruiter_list.html',{'recruiter_list':recruiter_list})

def studentapply(request,pk):
    if request.method == 'POST':
        form = CompaniesAppliedByStudentsForm(request.POST,initial={'user_id':request.user.id,'company_name':pk})
        if form.is_valid():
            form.save()
            return redirect('mywebsite:student')
    else:
        form = CompaniesAppliedByStudentsForm(initial={'user_id': request.user.id, 'company_name': pk})

    return render(request,'studentapply.html',{'form':form})




def addalumni(request):
    form = AlumniForm()
    if request.method == 'POST':
        form = AlumniForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:alumni')
    else:
        form = AlumniForm()
    return render(request,'AddAlumni.html',{'form':form})


def addresearch(request):
    form = ResearchForm()
    if request.method == 'POST':
        form = ResearchForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:research_development')
    else:
        form = ResearchForm()
    return render(request,'Addresearch.html',{'form':form})



def addteamimage(request):
    form = CollegeTeamImageForm()
    if request.method == 'POST':
        form = CollegeTeamImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:college_team')
    else:
        form = CollegeTeamImageForm()
    return render(request,'Addteamimage.html',{'form':form})



def addfacultyimage(request):
    form = CollegeTeamFacultyForm()
    if request.method == 'POST':
        form = CollegeTeamFacultyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:college_team')
    else:
        form = CollegeTeamFacultyForm()
    return render(request,'Addfacultyimage.html',{'form':form})




def addstudentimage(request):
    form = CollegeTeamStudentForm()
    if request.method == 'POST':
        form = CollegeTeamStudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:college_team')
    else:
        form = CollegeTeamStudentForm()
    return render(request,'Addstudentimage.html',{'form':form})




def addacademicimage(request):
    form =  AcademicImageForm()
    if request.method == 'POST':
        form =  AcademicImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:academic')
    else:
        form =  AcademicImageForm()
    return render(request,'Addacademicimage.html',{'form':form})




def addacademicvideo(request):
    form = AcademicVideoForm()
    if request.method == 'POST':
        form = AcademicVideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:academic')
    else:
        form = AcademicVideoForm()
    return render(request,'Addacademicvideo.html',{'form':form})




def addacademichighlight(request):
    form = AcademicHighlightForm()
    if request.method == 'POST':
        form = AcademicHighlightForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:academic')
    else:
        form = AcademicHighlightForm()
    return render(request,'Addacademichighlight.html',{'form':form})




def recruiter_quizlist(request):
    quizlist = Quiz.objects.filter(user_id = request.user.id)
    return render(request,'Recruiterquizlist.html',{'quizlist':quizlist})



