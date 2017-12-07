from django import forms
from django.forms.widgets import RadioSelect, Textarea
from quiz.models import Quiz


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


class CreatequizForm(forms.ModelForm):
    user_id = forms.IntegerField(widget = forms.HiddenInput())
    model = Quiz
    class Meta:
        fields = ('user_id','title','descriptiion','start_time','end_time','url','category','random_order','max_questions','answers_at_end',
                  'exam_paper','single_attempt','pass_mark','success_text','fail_text','draft')

