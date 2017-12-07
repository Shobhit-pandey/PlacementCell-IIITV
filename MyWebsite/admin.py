# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from true_false.models import TF_Question

from quiz.models import CategoryManager, Category, Question, Sitting, SittingManager, Progress, ProgressManager, Quiz, \
    SubCategory

from multichoice.models import MCQuestion, Answer

from essay.models import Essay_Question

admin.site.site_header = "TCP IIITV"
