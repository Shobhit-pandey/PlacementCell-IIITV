# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView

from resume.forms import ProjectFormset, ResumeForm, OtherFormset


def createresume(request, pk):
    referer = request.META.get('HTTP_REFERER')
    if referer == None:
        return render(request, 'quiz/wrongurl.html')
    project_formset = ProjectFormset()
    other_formset = OtherFormset()
    resume_form = ResumeForm(initial={'user_id': request.user.id})
    if request.method == "POST":
            print("-3")
            resume_form = ResumeForm(request.POST, initial={'user_id': request.user.id})
            if resume_form.is_valid():
                print("-4")
                resume_form.cleaned_data['user_id'] = request.user.id
                new_resume = resume_form.save()
                new_resume.save()
                print("1")
                project_formset = ProjectFormset(request.POST, instance=new_resume)
                other_formset = OtherFormset(request.POST, instance=new_resume)
                if project_formset.is_valid() and other_formset.is_valid():
                    print("2")
                    project_formset.save()
                    other_formset.save()
                    return redirect('mywebsite:student')
    else:
        resume_form = ResumeForm(request.POST, initial={'user_id': request.user.id})
        project_formset = ProjectFormset()
        other_formset = OtherFormset()
    return render(request, 'create_resume.html',
                  {'resume_form': resume_form, 'project_formset': project_formset,
                   'other_formset': other_formset,})