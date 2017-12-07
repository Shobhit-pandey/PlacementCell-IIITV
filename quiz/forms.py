from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils import timezone

from quiz.models import Quiz, Category


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))


class CreatequizForm(forms.Form):
    user_id=forms.CharField(max_length=100,required=True,widget=forms.HiddenInput())
    title = forms.CharField(max_length=100,required=True)
    description=forms.CharField(max_length=1000,required=True)
    start_time=forms.DateTimeField(required=True,initial=timezone.now())
    end_time=forms.DateTimeField(required=True,initial=timezone.now())
    url=forms.CharField(max_length=100,required=True)
    category=forms.ModelChoiceField(queryset=Category.objects.all(),required=True)
    random_order=forms.BooleanField(required=False)
    max_questions=forms.IntegerField(required=False)
    answers_at_end=forms.BooleanField(required=False)
    exam_paper=forms.BooleanField(required=False)
    single_attempt=forms.BooleanField(required=False)
    pass_mark=forms.IntegerField(required=False)
    success_text=forms.CharField(max_length=100,required=False)
    fail_text=forms.CharField(max_length=100,required=False)
    draft=forms.BooleanField(required=False)
    # user_id = forms.IntegerField()
    # class Meta:
    #     model = Quiz
    #     fields = ('title','description','start_time','end_time','url','category','random_order','max_questions','answers_at_end',
    #               'exam_paper','single_attempt','pass_mark','success_text','fail_text','draft')
    # def clean_start_time(self):
    #     start_time = self.cleaned_data.get('start_time')
    #     end_time = self.cleaned_data.get('end_time')
    #     if start_time < timezone.now():
    #         raise forms.ValidationError("start time should be in future")
    #     if start_time > end_time:
    #         raise forms.ValidationError("start time shold not after end time")
    #     return self.cleaned_data.get('start_time')

    def save(self,kwargs=None):
        u=Quiz.objects.create(
            user_id=self.cleaned_data.get('user_id'),
            title=self.cleaned_data.get('title'),
            description=self.cleaned_data.get('description'),
            start_time=self.cleaned_data.get('start_time'),
            end_time=self.cleaned_data.get('end_time'),
            url=self.cleaned_data.get('url'),
            category=self.cleaned_data.get('category'),
            random_order=self.cleaned_data.get('random_order'),
            max_questions=self.cleaned_data.get('max_questions'),
            answers_at_end=self.cleaned_data.get('answers_at_end'),
            exam_paper=self.cleaned_data.get('exam_paper'),
            single_attempt=self.cleaned_data.get('single_attempt'),
            pass_mark=self.cleaned_data.get('pass_mark'),
            success_text=self.cleaned_data.get('success_text'),
            fail_text=self.cleaned_data.get('fail_text'),
            draft=self.cleaned_data.get('draft'))
        u.save()
        return u
