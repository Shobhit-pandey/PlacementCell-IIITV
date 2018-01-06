from __future__ import unicode_literals
import re
import json
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import datetime

import django


@python_2_unicode_compatible
class Resume(models.Model):
    user_id = models.CharField(max_length=100, default="null")
    fullname = models.CharField(max_length=100, default="null")
    email = models.EmailField(null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    github = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = ("Resume")
        verbose_name_plural = ("Resumes")
        ordering = ['fullname']




@python_2_unicode_compatible
class Education(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))
    degree = models.CharField(max_length=100,
                              verbose_name=("Degree"),
                              blank=False)
    institute = models.CharField(max_length=1000,
                                 verbose_name=("Institute"),
                                 blank=False)
    year = models.CharField(max_length=20,
                            verbose_name=("Year"),
                            blank=False)
    cpi_aggreate = models.CharField(max_length=40,
                                    verbose_name=("Cpi"),
                                    blank=False)

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")


@python_2_unicode_compatible
class Skill(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))

    area_of_interest = models.CharField(max_length=1000,
                                        verbose_name=("AOI"),
                                        blank=False)
    programming_language = models.CharField(max_length=1000,
                                            verbose_name=("Programming"),
                                            blank=False)
    technical_elective = models.CharField(max_length=1000,
                                          verbose_name=("TechnicalElective"),
                                          blank=False)
    markup_language = models.CharField(max_length=1000,
                                       verbose_name=("MarkupLanguage"),
                                       blank=False)
    tool_techonology = models.CharField(max_length=1000,
                                        verbose_name=("ToolTechnology"),
                                        blank=False)
    database = models.CharField(max_length=1000,
                                verbose_name=("Database"),
                                blank=False)

    def __str__(self):
        return self.area_of_interest

    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")


@python_2_unicode_compatible
class Project(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))

    topic = models.CharField(max_length=100,
                             verbose_name=("Topic"),
                             blank=False)
    time = models.CharField(max_length=1000,
                            verbose_name=("Time"),
                            blank=False)
    team_size = models.IntegerField(blank=False)

    guide = models.CharField(max_length=1000,
                             verbose_name=("Guide"),
                             blank=False)
    description = models.CharField(max_length=500,
                                   verbose_name=("Description"),
                                   blank=False)
    project_link = models.URLField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")


@python_2_unicode_compatible
class Participation(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))
    topic = models.CharField(max_length=500,
                             verbose_name=("Participation"),
                             blank=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = ("Participation")
        verbose_name_plural = ("Participations")


@python_2_unicode_compatible
class PositionOfResponsibity(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))
    topic = models.CharField(max_length=500,
                             verbose_name=("PositionOfResponsibity"),
                             blank=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = ("PositionOfResponsibity")
        verbose_name_plural = ("PositionOfResponsibities")


@python_2_unicode_compatible
class AwardAchievement(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))
    topic = models.CharField(max_length=500,
                             verbose_name=("AwardAchievement"),
                             blank=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = ("AwardAchievement")
        verbose_name_plural = ("AwardAchievements")


@python_2_unicode_compatible
class Interest(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))
    topic = models.CharField(max_length=500,
                             verbose_name=("Interest"),
                             blank=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name =("Interest")
        verbose_name_plural = ("Interests")
