# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from MyWebsite.form import RecruiterForm, BeyondAcademicImagesForm, BeyondAcademicVideosForm, \
    BeyondAcademicHighlightForm, RecruiterInternshipIndustrialForm, RecruiterInternshipNGOForm, PastRecruiterForm, \
    CompaniesAppliedByStudentsForm, AlumniForm, ResearchForm, CollegeTeamImageForm, CollegeTeamFacultyForm, \
    CollegeTeamStudentForm, AcademicImageForm, AcademicVideoForm, AcademicHighlightForm, AddStudent, AddRecruiter, \
    PastRecruitersSelectionForm
from MyWebsite.models import BeyondAcademicImages, BeyondAcademicVideos, BeyondAcademicsHighlight, PastRecruiter, \
    RecruiterInternshipIndustrial, RecruiterInternshipNGO, Recruiter, CollegeTeamImage, CollegeTeamFaculty, \
    CollegeTeamStudent, Alumni, Research, AcademicImage, AcademicVideo, AcademicHighlight, CompaniesAppliedByStudents, \
    PastRecruitersSelection
from quiz.models import Quiz

from django.contrib import messages


def home(request):
    pastrecruiter = PastRecruitersSelection.objects.all()
    return render(request, 'home.html', {'pastimage': pastrecruiter})


def student(request):
    return render(request, 'Student.html')


def recruiter(request):
    images = PastRecruiter.objects.all()
    industrials = RecruiterInternshipIndustrial.objects.all()
    ngos = RecruiterInternshipNGO.objects.all()
    return render(request, 'Recruiter.html', {'images': images, 'industrials': industrials, 'ngos': ngos})


def about(request):
    return render(request, 'About.html')


def procedure(request):
    return render(request, 'Procedure.html')


def academic(request):
    addacademicimage = AcademicImage.objects.all()
    addacademicvideo = AcademicVideo.objects.all()
    addacademichighlight = AcademicHighlight.objects.all()
    return render(request, 'Academic.html', {'addacademicimage': addacademicimage, 'addacademicvideo': addacademicvideo,
                                             'addacademichighlight': addacademichighlight})


def college_team(request):
    addteamimage = CollegeTeamImage.objects.all()
    addfacultyimage = CollegeTeamFaculty.objects.all()
    addstudentimage = CollegeTeamStudent.objects.all()

    return render(request, 'college_team.html', {'addteamimage': addteamimage, 'addfacultyimage': addfacultyimage,
                                                 'addstudentimage': addstudentimage})


def contact(request):
    return render(request, 'Contact.html')


def department(request):
    return render(request, 'departments.html')


def alumni(request):
    alumnis = Alumni.objects.all()
    return render(request, 'alumni.html', {'alumnis': alumnis})


def research_development(request):
    researchs = Research.objects.all()
    return render(request, 'research_development.html', {'researchs': researchs})


@csrf_protect
def recruiter_form(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            value = form.save()
            email = form.cleaned_data['email']
            contact = form.cleaned_data['Contact_Number']

            name = form.cleaned_data['Name']
            value.save()
            email = EmailMessage('Regarding Admission',
                                 "Hey " + "we have received your mail we will contact you on" + str(contact) +
                                 str(email),
                                 to=[email,
                                     'studymonk.se@gmail.com'],
                                 reply_to=["studymonk.se@gmail.com", ])
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
    return render(request, 'beyond_academics.html', {'image': image, 'video': video, 'highlight': highlight})


def add_beyond_academic_images(request):
    if request.method == 'POST':
        form = BeyondAcademicImagesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicImagesForm()
    return render(request, 'AddBeyondAcademicImage.html', {'form': form})


def add_beyond_academic_videos(request):
    if request.method == 'POST':
        form = BeyondAcademicVideosForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicVideosForm()
    return render(request, 'AddBeyondAcademicVideo.html', {'form': form})


def add_beyond_academic_highlight(request):
    if request.method == "POST":
        form = BeyondAcademicHighlightForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:beyond_academic')
    else:
        form = BeyondAcademicHighlightForm()
    return render(request, 'AddBeyondAcademicHighlight.html', {'form': form})


def add_intern_descrip(request):
    if request.method == 'POST':
        form = RecruiterInternshipIndustrialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mywebsite:recruiter')

    else:
        form = RecruiterInternshipIndustrialForm()
    return render(request, 'AddRecruiterInternshipIndustrial.html', {'form': form})


def add_ngo_descrip(request):
    if request.method == 'POST':
        form = RecruiterInternshipNGOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:recruiter')

    else:
        form = RecruiterInternshipNGOForm()
    return render(request, 'AddRecruiterInternshipNGO.html', {'form': form})


def add_past_recruiter_image(request):
    if request.method == 'POST':
        form = PastRecruiterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:recruiter')

    else:
        form = PastRecruiterForm()
    return render(request, 'Addpastrecuiter.html', {'form': form})


def add_pastrecruiters_image(request):
    if request.method == 'POST':
        form = PastRecruitersSelectionForm(request.POST, request.FILES)
        if form.is_valid():
            PastRecruitersSelection.objects.all().delete()
            form.save()
            return redirect('mywebsite:home')

    else:
        form = PastRecruitersSelectionForm()
    return render(request, 'addmultiplerecruiter.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("mywebsite:recruiter")
        else:
            form = PasswordChangeForm(user=request.user)
            messages.info(request, 'Wrong Attempt!')
            return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}

        return render(request, 'change_password.html', {'form': form})


def recruiter_listview(request):
    list = CompaniesAppliedByStudents.objects.filter(user_id=request.user.id).values_list('company_name')
    lists = []
    for x in range(0, len(list)):
        lists.append(int(list[x][0]))
    recruiter_list = Recruiter.objects.all()
    return render(request, 'recruiter_list.html', {'recruiter_list': recruiter_list, 'lists': lists})


def studentapply(request, pk):
    recruiters = Recruiter.objects.filter(id=pk)
    if request.method == 'POST':
        form = CompaniesAppliedByStudentsForm(request.POST, initial={'user_id': request.user.id, 'company_name': pk,
                                                                     'roll_number': request.user.username})
        if form.is_valid():
            form.save()
            return redirect('mywebsite:student')
    else:
        form = CompaniesAppliedByStudentsForm(
            initial={'user_id': request.user.id, 'company_name': pk, 'roll_number': request.user.username})

    return render(request, 'studentapply.html', {'form': form, 'recruiters': recruiters})


def addalumni(request):
    form = AlumniForm()
    if request.method == 'POST':
        form = AlumniForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:alumni')
    else:
        form = AlumniForm()
    return render(request, 'AddAlumni.html', {'form': form})


def addresearch(request):
    form = ResearchForm()
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:research_development')
    else:
        form = ResearchForm()
    return render(request, 'Addresearch.html', {'form': form})


def addteamimage(request):
    form = CollegeTeamImageForm()
    if request.method == 'POST':
        form = CollegeTeamImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:college_team')
    else:
        form = CollegeTeamImageForm()
    return render(request, 'Addteamimage.html', {'form': form})


def addfacultyimage(request):
    form = CollegeTeamFacultyForm()
    if request.method == 'POST':
        form = CollegeTeamFacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:college_team')
    else:
        form = CollegeTeamFacultyForm()
    return render(request, 'Addfacultyimage.html', {'form': form})


def addstudentimage(request):
    form = CollegeTeamStudentForm()
    if request.method == 'POST':
        form = CollegeTeamStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:college_team')
    else:
        form = CollegeTeamStudentForm()
    return render(request, 'Addstudentimage.html', {'form': form})


def addacademicimage(request):
    form = AcademicImageForm()
    if request.method == 'POST':
        form = AcademicImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:academic')
    else:
        form = AcademicImageForm()
    return render(request, 'Addacademicimage.html', {'form': form})


def addacademicvideo(request):
    form = AcademicVideoForm()
    if request.method == 'POST':
        form = AcademicVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:academic')
    else:
        form = AcademicVideoForm()
    return render(request, 'Addacademicvideo.html', {'form': form})


def addacademichighlight(request):
    form = AcademicHighlightForm()
    if request.method == 'POST':
        form = AcademicHighlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mywebsite:academic')
    else:
        form = AcademicHighlightForm()
    return render(request, 'Addacademichighlight.html', {'form': form})


def recruiter_quizlist(request):
    quizlist = Quiz.objects.filter(user_id=request.user.id)
    return render(request, 'Recruiterquizlist.html', {'quizlist': quizlist})


# recruiter shortlised by student
def student_shortlisted_recruiter(request):
    list = CompaniesAppliedByStudents.objects.filter(user_id=request.user.id)
    recruiter_list = Recruiter.objects.all()
    return render(request, 'student_recruiter_list.html', {'lists': list, 'recruiter_list': recruiter_list})


# student applied list in recruiter form
def recruiter_shortlisted_student(request):
    list = CompaniesAppliedByStudents.objects.all()
    recruiter_list = Recruiter.objects.filter()
    return render(request, 'recruiter_shortlisted_student.html', {'lists': list, 'recruiter_list': recruiter_list})


def recruiter_shortlisted_student_superuser(request, pk1):
    students = CompaniesAppliedByStudents.objects.filter(company_name=pk1)
    return render(request, 'recruiter_shortlisted_student_superuser.html', {'students': students})


def addstudent(request):
    form = AddStudent()
    if request.method == 'POST':
        form = AddStudent(request.POST, initial={'is_staff': False})
        if form.is_valid():
            user = form.save()
            user.is_staff = False
            user.is_superuser = False
            user.save()
            return redirect('mywebsite:home')

    else:
        form = AddStudent()
    return render(request, 'addstudent.html', {'form': form})


def addrecruiter(request):
    form = AddRecruiter()
    if request.method == 'POST':
        form = AddRecruiter(request.POST, initial={'is_staff': True})
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.is_superuser = False
            user.save()
            return redirect('mywebsite:home')

    else:
        form = AddRecruiter()
    return render(request, 'addrecruiter.html', {'form': form})
