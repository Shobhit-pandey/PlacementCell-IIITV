from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils import timezone
from django.forms.models import inlineformset_factory

from essay.models import Essay_Question

from true_false.models import TF_Question

from multichoice.models import MCQuestion, Answer

from quiz.models import Quiz, Category, SubCategory

ANSWER_ORDER_OPTIONS = (
    ('content', ('Content')),
    ('random', ('Random')),
    ('none', ('None'))
)


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
    user_id = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=1000, required=True)
    start_time = forms.DateTimeField(required=True, initial=timezone.now())
    end_time = forms.DateTimeField(required=True, initial=timezone.now())
    url = forms.CharField(max_length=100, required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    random_order = forms.BooleanField(required=False)
    max_questions = forms.IntegerField(required=False)
    answers_at_end = forms.BooleanField(required=False)
    exam_paper = forms.BooleanField(required=False)
    single_attempt = forms.BooleanField(required=False)
    pass_mark = forms.IntegerField(required=False, initial=0)
    success_text = forms.CharField(max_length=100, required=False)
    fail_text = forms.CharField(max_length=100, required=False)
    draft = forms.BooleanField(required=False)

    def save(self, kwargs=None):
        u = Quiz.objects.create(
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


class MCQuestionForm(forms.Form):
    user_id = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=False)
    figure = forms.ImageField(required=False)
    content = forms.CharField(max_length=1000, required=True)
    explanation = forms.CharField(max_length=2000, required=False)
    answer_order = forms.ChoiceField(ANSWER_ORDER_OPTIONS, required=True)

    def save(self):
        u = MCQuestion.objects.create(
            sub_category=self.cleaned_data.get('sub_category'),
            user_id=self.cleaned_data.get('user_id'),
            figure=self.cleaned_data.get('figure'),
            content=self.cleaned_data.get('content'),
            explanation=self.cleaned_data.get('explanation'),
            answer_order=self.cleaned_data.get('answer_order')
        )
        u.save()
        return u


# class MCQuestionForm(forms.ModelForm):
#     class Meta:
#         model=MCQuestion
#         fields=('sub_category','user_id','figure','content','explanation','answer_order')
#         exclude = []

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', 'correct')
        exclude = []


MCQFormSet = inlineformset_factory(MCQuestion, Answer, form=AnswerForm, can_delete=False)


class TFForm(forms.Form):
    user_id = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=False)
    figure = forms.ImageField(required=False)
    content = forms.CharField(max_length=1000, required=True)
    explanation = forms.CharField(max_length=2000, required=False)
    correct = forms.BooleanField(required=False)

    def save(self):
        u = TF_Question.objects.create(
            sub_category=self.cleaned_data.get('sub_category'),
            user_id=self.cleaned_data.get('user_id'),
            figure=self.cleaned_data.get('figure'),
            content=self.cleaned_data.get('content'),
            explanation=self.cleaned_data.get('explanation'),
            correct=self.cleaned_data.get('correct')
        )
        u.save()
        return u


class EssayEForm(forms.Form):
    user_id = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=False)
    figure = forms.ImageField(required=False)
    content = forms.CharField(max_length=1000, required=True)
    explanation = forms.CharField(max_length=2000, required=False)

    # correct=forms.BooleanField()

    def save(self):
        u = Essay_Question.objects.create(
            sub_category=self.cleaned_data.get('sub_category'),
            user_id=self.cleaned_data.get('user_id'),
            figure=self.cleaned_data.get('figure'),
            content=self.cleaned_data.get('content'),
            explanation=self.cleaned_data.get('explanation'),
        )
        u.save()
        return u
