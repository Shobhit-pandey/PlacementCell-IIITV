from django import forms

from MyWebsite.models import Recruiter, BeyondAcademicImages, BeyondAcademicVideos, BeyondAcademicsHighlight, \
    RecruiterInternshipIndustrial, RecruiterInternshipNGO, PastRecruiter


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude=[]
class PastRecruiterForm(forms.ModelForm):
    class Meta:
        model = PastRecruiter
        exclude=[]


class BeyondAcademicImagesForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicImages
        exclude=[]



class BeyondAcademicVideosForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicVideos
        exclude=[]



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

