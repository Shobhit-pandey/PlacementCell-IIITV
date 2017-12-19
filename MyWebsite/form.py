from django import forms
from django.contrib.auth.models import User

from MyWebsite.models import Recruiter, BeyondAcademicImages, BeyondAcademicVideos, BeyondAcademicsHighlight, \
    RecruiterInternshipIndustrial, RecruiterInternshipNGO, PastRecruiter, CompaniesAppliedByStudents, Alumni, Research, \
    CollegeTeamImage, CollegeTeamStudent, CollegeTeamFaculty, AcademicImage, AcademicVideo, AcademicHighlight


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude = []


class PastRecruiterForm(forms.ModelForm):
    class Meta:
        model = PastRecruiter
        exclude = []


class BeyondAcademicImagesForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicImages
        exclude = []


class BeyondAcademicVideosForm(forms.ModelForm):
    class Meta:
        model = BeyondAcademicVideos
        exclude = []


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
    user_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
    roll_number = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(), initial="rollnumber")
    company_name = forms.IntegerField(required=True, widget=forms.HiddenInput())

    def save(self):
        u = CompaniesAppliedByStudents.objects.create(
            user_id=self.cleaned_data.get('user_id'),
            roll_number=self.cleaned_data.get('roll_number'),
            company_name=self.cleaned_data.get('company_name'),

        )
        u.save()
        return u;


class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        exclude = []


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        exclude = []


class CollegeTeamImageForm(forms.ModelForm):
    class Meta:
        model = CollegeTeamImage
        exclude = []


class CollegeTeamFacultyForm(forms.ModelForm):
    class Meta:
        model = CollegeTeamFaculty
        exclude = []


class CollegeTeamStudentForm(forms.ModelForm):
    class Meta:
        model = CollegeTeamStudent
        exclude = []


class AcademicImageForm(forms.ModelForm):
    class Meta:
        model = AcademicImage
        exclude = []


class AcademicVideoForm(forms.ModelForm):
    class Meta:
        model = AcademicVideo
        exclude = []


class AcademicHighlightForm(forms.ModelForm):
    class Meta:
        model = AcademicHighlight
        exclude = []


class AddRecruiter(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    def save(self):
        u = User.objects.create_user(username=self.cleaned_data.get('username'),
                                     password=self.cleaned_data.get('password'),
                                     email=self.cleaned_data.get('email'),
                                     )
        u.save()
        return u


class AddStudent(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    def save(self):
        u = User.objects.create_user(username=self.cleaned_data.get('username'),
                                     password=self.cleaned_data.get('password'),
                                     email=self.cleaned_data.get('email'),
                                     )
        u.save()
        return u
