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

from resume.forms import EducationFormset, SkillFormset, ProjectFormset, ParticipationFormset, \
    PositionOfResponsibityFormset, AwardAchievementFormset, InterestFormset, ResumeForm


def createresume(request, pk):
    referer = request.META.get('HTTP_REFERER')
    if referer == None:
        return render(request, 'quiz/wrongurl.html')
    education_formset = EducationFormset()
    skill_formset = SkillFormset()
    project_formset = ProjectFormset()
    participation_formset = ParticipationFormset()
    position_of_responsibity_formset = PositionOfResponsibityFormset()
    award_achievement_formset = AwardAchievementFormset()
    interest_formset = InterestFormset()
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
                education_formset = EducationFormset(request.POST, instance=new_resume)
                skill_formset = SkillFormset(request.POST, instance=new_resume)
                project_formset = ProjectFormset(request.POST, instance=new_resume)
                participation_formset = ParticipationFormset(request.POST, instance=new_resume)
                position_of_responsibity_formset = PositionOfResponsibityFormset(request.POST, instance=new_resume)
                award_achievement_formset = AwardAchievementFormset(request.POST, instance=new_resume)
                interest_formset = InterestFormset(request.POST, instance=new_resume)
                if education_formset.is_valid() and skill_formset.is_valid() and project_formset.is_valid() and participation_formset.is_valid() and position_of_responsibity_formset.is_valid() and award_achievement_formset.is_valid() and interest_formset.is_valid():
                    print("2")
                    education_formset.save()
                    skill_formset.save()
                    project_formset.save()
                    participation_formset.save()
                    position_of_responsibity_formset.save()
                    award_achievement_formset.save()
                    interest_formset.save()
                    return redirect('mywebsite:student')
    else:
        resume_form = ResumeForm(request.POST, initial={'user_id': request.user.id})
        education_formset = EducationFormset()
        skill_formset = SkillFormset()
        project_formset = ProjectFormset()
        participation_formset = ParticipationFormset()
        position_of_responsibity_formset = PositionOfResponsibityFormset()
        award_achievement_formset = AwardAchievementFormset()
        interest_formset = InterestFormset()
    return render(request, 'create_resume.html',
                  {'resume_form': resume_form, 'education_formset': education_formset,
                   'skill_formset': skill_formset, 'project_formset': project_formset,
                   'participation_formset': participation_formset,
                   'position_of_responsibity_formset': position_of_responsibity_formset,
                   'award_achievement_formset': award_achievement_formset, 'interest_formset': interest_formset})