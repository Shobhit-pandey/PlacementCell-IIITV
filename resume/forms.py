from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils import timezone
from django.forms.models import inlineformset_factory

from resume.models import Resume, Education, Skill, Project, Participation, PositionOfResponsibity, AwardAchievement, \
    Interest


class ResumeForm(forms.Form):
    user_id = forms.CharField(max_length=100, required=True,initial="0")
    fullname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    dob = forms.DateField(required=True)
    github = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)

    def save(self):
        r = Resume.objects.create(
            user_id=self.cleaned_data.get('user_id'),
            fullname=self.cleaned_data.get('fullname'),
            email=self.cleaned_data.get('email'),
            dob=self.cleaned_data.get('dob'),
            github=self.cleaned_data.get('github'),
            linkedin=self.cleaned_data.get('linkedin'),
        )
        r.save()
        return r


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('degree', 'institute', 'year', 'cpi_aggreate')
        exclude = []


EducationFormset = inlineformset_factory(Resume, Education, form=EducationForm, can_delete=True, extra=1)


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = (
            'area_of_interest', 'programming_language', 'technical_elective', 'markup_language', 'tool_techonology',
            'database')
        exclude = []


SkillFormset = inlineformset_factory(Resume, Skill, form=SkillForm, can_delete=True, extra=1)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'topic', 'time', 'team_size', 'guide', 'description',
            'project_link')
        exclude = []


ProjectFormset = inlineformset_factory(Resume, Project, form=ProjectForm, can_delete=True, extra=1)


class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ('topic',)
        exclude = []


ParticipationFormset = inlineformset_factory(Resume, Participation, form=ParticipationForm, can_delete=True, extra=1)


class PositionOfResponsibityForm(forms.ModelForm):
    class Meta:
        model = PositionOfResponsibity
        fields = ('topic',)
        exclude = []


PositionOfResponsibityFormset = inlineformset_factory(Resume, PositionOfResponsibity, form=PositionOfResponsibityForm,
                                                      can_delete=True, extra=1)


class AwardAchievementForm(forms.ModelForm):
    class Meta:
        model = AwardAchievement
        fields = ('topic',)
        exclude = []


AwardAchievementFormset = inlineformset_factory(Resume, AwardAchievement, form=AwardAchievementForm, can_delete=True,
                                                extra=1)


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ('topic',)
        exclude = []


InterestFormset = inlineformset_factory(Resume, Interest, form=InterestForm, can_delete=True, extra=2)
