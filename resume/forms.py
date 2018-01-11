from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils import timezone
from django.forms.models import inlineformset_factory

from resume.models import Resume, Project, Other


class ResumeForm(forms.Form):
    user_id = forms.CharField(max_length=100, required=True, initial="0")
    fullname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    dob = forms.DateField(required=True,help_text="YYYY-MM-DD")
    github = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    class_ten_institute = forms.CharField(max_length=1000, required=True)
    class_ten_passing_year = forms.CharField(max_length=20, required=True)
    class_ten_cgpa = forms.CharField(max_length=40, required=True)
    class_twelve_institute = forms.CharField(max_length=1000, required=True)
    class_twelve_passing_year = forms.CharField(max_length=20, required=True)
    class_twelve_percentage = forms.CharField(max_length=40, required=True)
    btech_institute = forms.CharField(max_length=1000, required=True)
    btech_cpi = forms.CharField(max_length=40, required=True)
    btech_batch = forms.CharField(max_length=40, required=True)
    mtech_institute = forms.CharField(max_length=1000, required=False)
    mtech_cpi = forms.CharField(max_length=40, required=False)
    mtech_batch = forms.CharField(max_length=40, required=False)
    area_of_interest = forms.CharField(max_length=1000, required=True)
    programming_language = forms.CharField(max_length=1000, required=True)
    technical_elective = forms.CharField(max_length=1000, required=True)
    markup_language = forms.CharField(max_length=1000, required=True)
    tool_techonology = forms.CharField(max_length=1000, required=True)
    database = forms.CharField(max_length=1000, required=True)

    def save(self):
        r = Resume.objects.create(
            user_id=self.cleaned_data.get('user_id'),
            fullname=self.cleaned_data.get('fullname'),
            email=self.cleaned_data.get('email'),
            dob=self.cleaned_data.get('dob'),
            github=self.cleaned_data.get('github'),
            linkedin=self.cleaned_data.get('linkedin'),
            class_ten_institute=self.cleaned_data.get('class_ten_institute'),
            class_ten_passing_year=self.cleaned_data.get('class_ten_passing_year'),
            class_ten_cgpa=self.cleaned_data.get('class_ten_cgpa'),
            class_twelve_institute=self.cleaned_data.get('class_twelve_institute'),
            class_twelve_passing_year=self.cleaned_data.get('class_twelve_passing_year'),
            class_twelve_percentage=self.cleaned_data.get('class_twelve_percentage'),
            btech_institute=self.cleaned_data.get('btech_institute'),
            btech_cpi=self.cleaned_data.get('btech_cpi'),
            btech_batch=self.cleaned_data.get('btech_batch'),
            mtech_institute=self.cleaned_data.get('mtech_institute'),
            mtech_cpi=self.cleaned_data.get('mtech_cpi'),
            mtech_batch=self.cleaned_data.get('mtech_batch'),
            area_of_interest=self.cleaned_data.get('area_of_interest'),
            programming_language=self.cleaned_data.get('programming_language'),
            technical_elective=self.cleaned_data.get('technical_elective'),
            markup_language=self.cleaned_data.get('markup_language'),
            tool_techonology=self.cleaned_data.get('tool_techonology'),
            database=self.data.get('database'),
        )
        r.save()
        return r


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'topic', 'time', 'team_size', 'guide', 'description',
            'project_link')
        exclude = []


ProjectFormset = inlineformset_factory(Resume, Project, form=ProjectForm, can_delete=True, extra=1)


class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ('choice', 'topic')
        exclude = []


OtherFormset = inlineformset_factory(Resume, Other, form=OtherForm, can_delete=True, extra=1)
