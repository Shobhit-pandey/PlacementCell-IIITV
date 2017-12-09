from django import forms

from MyWebsite.models import Recruiter, BeyondAcademicImages, BeyondAcademicVideos, BeyondAcademicsHighlight, \
    RecruiterInternshipIndustrial, RecruiterInternshipNGO, PastRecruiter, CompaniesAppliedByStudents, Alumni, Research


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



class CompaniesAppliedByStudentsForm(forms.Form):
    user_id = forms.CharField(max_length=50,required=True,widget=forms.HiddenInput())
    roll_number = forms.CharField(max_length=20,required=True)
    company_name = forms.CharField(max_length=250,required=True,widget=forms.HiddenInput())

    def save(self):
        u = CompaniesAppliedByStudents.objects.create(
            user_id = self.cleaned_data.get('user_id'),
            roll_number = self.cleaned_data.get('roll_number'),
            company_name = self.cleaned_data.get('company_name'),

        )



class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        exclude = []


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        exclude = []

















