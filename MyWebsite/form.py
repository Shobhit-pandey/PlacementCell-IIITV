from django import forms

from MyWebsite.models import Recruiter


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude=[]