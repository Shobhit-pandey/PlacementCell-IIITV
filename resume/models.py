from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import datetime
from froala_editor.fields import FroalaField

CHOICE = (
    ('Participation', 'Participation'),
    ('Position Of Responsibity', ('Position Of Responsibity')),
    ('Award Achievement', 'Award Achievement'),
    ('Interest', 'Interest'),
    ('PastExperience', 'PastExperience'),
)


@python_2_unicode_compatible
class Resume(models.Model):
    user_id = models.CharField(max_length=100, default="null")
    fullname = models.CharField(max_length=100, default="null")
    email = models.EmailField(null=False, blank=False)
    dob = models.DateField(null=False, blank=False, help_text="YYYY-MM-DD", default=datetime.today())
    github = models.URLField()
    linkedin = models.URLField()
    class_ten_institute = models.CharField(max_length=1000, blank=False)
    class_ten_passing_year = models.CharField(max_length=20, blank=False)
    class_ten_cgpa = models.CharField(max_length=40, blank=False)
    class_twelve_institute = models.CharField(max_length=1000, blank=False)
    class_twelve_passing_year = models.CharField(max_length=20, blank=False)
    class_twelve_percentage = models.CharField(max_length=40, blank=False)
    btech_institute = models.CharField(max_length=1000, blank=False)
    btech_cpi = models.CharField(max_length=40, blank=False)
    btech_batch = models.CharField(max_length=40, blank=False)
    mtech_institute = models.CharField(max_length=1000, blank=False)
    mtech_cpi = models.CharField(max_length=40, blank=False)
    mtech_batch = models.CharField(max_length=40, blank=False)
    area_of_interest = models.CharField(max_length=1000, blank=False)
    programming_language = models.CharField(max_length=1000, blank=False)
    technical_elective = models.CharField(max_length=1000, blank=False)
    markup_language = models.CharField(max_length=1000, blank=False)
    tool_techonology = models.CharField(max_length=1000, blank=False)
    database = models.CharField(max_length=1000, blank=False)
    resume_created = models.DateField(null=True, blank=True, default=datetime.now())

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = ("Resume")
        verbose_name_plural = ("Resumes")
        ordering = ['fullname']


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
    description = models.TextField(max_length=500,
                                   verbose_name=("Description"),
                                   blank=False)
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")


@python_2_unicode_compatible
class Other(models.Model):
    resume = models.ForeignKey(Resume, verbose_name=("Resume"))
    choice = models.CharField(
        max_length=30, null=True, blank=True,
        choices=CHOICE, default='Participation')
    topic = models.TextField( verbose_name="Other", blank=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = ("Other")
        verbose_name_plural = ("Others")
