from django import forms

from MyWebsite.models import Recruiter,BeyondAcademicImages,BeyondAcademicVideos


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude=[]



class BeyondAcademicImagesForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicImages
        exclude=[]



class BeyondAcademicVideosForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicVideos
        exclude=[]


