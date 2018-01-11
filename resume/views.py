# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import RequestContext
from datetime import datetime

from resume.forms import ProjectFormset, ResumeForm, OtherFormset
from resume.models import Resume, Project, Other


def resume(request, pk2):
    users = User.objects.filter(username=pk2)
    resumes = Resume.objects.all()
    projects = Project.objects.all()
    current = datetime.now().date()
    participations = Other.objects.filter(choice="Participation")
    position_of_responsibity = Other.objects.filter(choice="Position of Responsibity")
    awards = Other.objects.filter(choice="Award Achievement")
    interests = Other.objects.filter(choice="Interest")
    return render(request, 'Resume.html', {'users': users, 'resumes': resumes, 'projects': projects, 'current': current,
                                           'participations': participations,
                                           'position_of_responsibity': position_of_responsibity, 'awards': awards, 'interests' : interests})


def delete_resume(request):
    resume = Resume.objects.filter(user_id=request.user.id)
    list = []
    for resu in resume:
        list.append(resu.id)
    resume.delete()
    for x in list:
        projects = Project.objects.filter(resume_id=x)
        other = Other.objects.filter(resume_id=x)
        projects.delete()
        other.delete()
    return render(request, 'delete_resume.html')


def createresume(request, pk):
    resumes = Resume.objects.filter(user_id=request.user.id)
    referer = request.META.get('HTTP_REFERER')
    if referer == None:
        return render(request, 'quiz/wrongurl.html')
    project_formset = ProjectFormset()
    other_formset = OtherFormset()
    resume_form = ResumeForm(initial={'user_id': request.user.id})
    if request.method == "POST":
        resume_form = ResumeForm(request.POST, initial={'user_id': request.user.id})
        if resume_form.is_valid():
            resume_form.cleaned_data['user_id'] = request.user.id
            new_resume = resume_form.save()
            new_resume.save()
            project_formset = ProjectFormset(request.POST, instance=new_resume)
            other_formset = OtherFormset(request.POST, instance=new_resume)
            if project_formset.is_valid() and other_formset.is_valid():
                project_formset.save()
                other_formset.save()
                return redirect('mywebsite:student')
    else:
        resume_form = ResumeForm(request.POST, initial={'user_id': request.user.id})
        project_formset = ProjectFormset()
        other_formset = OtherFormset()
    return render(request, 'create_resume.html',
                  {'resume_form': resume_form, 'project_formset': project_formset,
                   'other_formset': other_formset, 'resumes': resumes, },
                  context_instance=RequestContext(request))
