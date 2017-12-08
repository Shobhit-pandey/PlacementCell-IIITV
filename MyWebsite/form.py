from django import forms

from MyWebsite.models import Recruiter,BeyondAcademicImages,BeyondAcademicVideos,BeyondAcademicsHighlight,RecruiterInternshipIndustrial,RecruiterInternshipNGO


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude=[]



class BeyondAcademicImagesForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicImages



class BeyondAcademicVideosForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicVideos



class BeyondAcademicHighlightForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicsHighlight
        exclude = []



class RecruiterInternshipIndustrialForm(forms.ModelForm):
    class Meta:
        model = RecruiterInternshipIndustrial
        exclude = []


class RecruiterInternshipNGOForm(forms.ModelForm):
    class Meta:
        model = RecruiterInternshipNGO
        exclude = []



