# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from MyWebsite.models import Recruiter, Gallery, PastRecruiter, BeyondAcademicImages, BeyondAcademicVideos, \
    BeyondAcademicsHighlight, RecruiterInternshipIndustrial, RecruiterInternshipNGO, CompaniesAppliedByStudents, Alumni, \
    Research
from true_false.models import TF_Question

from quiz.models import CategoryManager, Category, Question, Sitting, SittingManager, Progress, ProgressManager, Quiz, \
    SubCategory

from multichoice.models import MCQuestion, Answer

from essay.models import Essay_Question

admin.site.site_header = "TCP IIITV"

admin.site.register(Recruiter)
admin.site.register(Gallery)
admin.site.register(PastRecruiter)
# admin.site.register(SelectionProcess)
admin.site.register(BeyondAcademicImages)
admin.site.register(BeyondAcademicVideos)
admin.site.register(BeyondAcademicsHighlight)
admin.site.register(RecruiterInternshipIndustrial)
admin.site.register(RecruiterInternshipNGO)
admin.site.register(CompaniesAppliedByStudents)
admin.site.register(Alumni)
admin.site.register(Research)
