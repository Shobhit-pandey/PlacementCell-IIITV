# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import copy
from wkhtmltopdf.views import PDFTemplateResponse, PDFTemplateView

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from datetime import datetime

from django.template.loader import get_template
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin, ContextMixin

from resume.forms import ProjectFormset, ResumeForm, OtherFormset
from resume.models import Resume, Project, Other
from resume.utils import render_to_pdf


def resume(request, pk2):
    wrong = "USER NOT FOUND"
    try:
        users = User.objects.filter(username=pk2)
        u = User.objects.get(username=pk2)
    except:
        return render(request, 'wrong.html', {'wrong': wrong})
    try:
        resumes = Resume.objects.filter(user_id=u.id)
        r = Resume.objects.get(user_id=u.id)
    except:
        wrong = "RESUME EITHER DELETED OR NOT CREATED"
        return render(request, 'wrong.html', {'wrong': wrong})
    # resumes = Resume.objects.all()
    projects = Project.objects.filter(resume_id=r.id)
    # projects = Project.objects.all()
    current = datetime.now().date()
    participations = Other.objects.filter(choice="Participation", resume_id=r.id)
    position_of_responsibity = Other.objects.filter(choice="Position of Responsibity", resume_id=r.id)
    awards = Other.objects.filter(choice="Award Achievement", resume_id=r.id)
    interests = Other.objects.filter(choice="Interest", resume_id=r.id)
    resume_name = pk2
    return render(request, 'Resume.html', {'users': users, 'resumes': resumes, 'projects': projects, 'current': current,
                                           'participations': participations,
                                           'position_of_responsibity': position_of_responsibity, 'awards': awards,
                                           'interests': interests, 'resume_name': resume_name})


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


# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#
#         }
#         pdf = render_to_pdf('pdf/Resume.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

def generate_pdf(request, pk3):
    users = User.objects.filter(username=pk3)
    u = User.objects.get(username=pk3)
    resumes = Resume.objects.filter(user_id=u.id)
    r = Resume.objects.get(user_id=u.id)
    projects = Project.objects.filter(resume_id=r.id)
    # projects = Project.objects.all()
    current = datetime.now().date()
    participations = Other.objects.filter(choice="Participation", resume_id=r.id)
    position_of_responsibity = Other.objects.filter(choice="Position of Responsibity", resume_id=r.id)
    awards = Other.objects.filter(choice="Award Achievement", resume_id=r.id)
    interests = Other.objects.filter(choice="Interest", resume_id=r.id)
    template = get_template('pdf/Resume.html')
    context = {
        "users": users,
        "resumes": resumes,
        "projects": projects,
        "current": current,
        "participations": participations,
        "position_of_responsibity": position_of_responsibity,
        "awards": awards,
        "interests": interests,
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf/Resume.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Resume_%s.pdf" % ("12341231")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def pdf(request, pk4):
    users = User.objects.filter(username=pk4)
    u = User.objects.get(username=pk4)
    resumes = Resume.objects.filter(user_id=u.id)
    r = Resume.objects.get(user_id=u.id)
    projects = Project.objects.filter(resume_id=r.id)
    # projects = Project.objects.all()
    current = datetime.now().date()
    participations = Other.objects.filter(choice="Participation", resume_id=r.id)
    position_of_responsibity = Other.objects.filter(choice="Position of Responsibity", resume_id=r.id)
    awards = Other.objects.filter(choice="Award Achievement", resume_id=r.id)
    interests = Other.objects.filter(choice="Interest", resume_id=r.id)
    context = RequestContext(request)
    template = 'pdf/Resume.html'

    context = {
        "users": users,
        "resumes": resumes,
        "projects": projects,
        "current": current,
        "participations": participations,
        "position_of_responsibity": position_of_responsibity,
        "awards": awards,
        "interests": interests,
    }
    return PDFTemplateResponse(request=request, cmd_options={'disable-javascript': True}, template=template,filename=(str)(pk4)+"_resume.pdf",
                           context=context)