from django import forms

from discussion.models import ShareReply, Share


class ShareReplyForm(forms.ModelForm):
    class Meta:
        model = ShareReply
        fields = ['content', 'share', 'user']

    def clean_content(self):
        return self.cleaned_data.get('content')

    def clean_share(self):
        return self.cleaned_data.get('share')

    def clean_user(self):
        return self.cleaned_data.get('user')

class ShareRepliesForm(forms.ModelForm):
    class Meta:
        model = ShareReply
        fields = ['content',]

    def clean_content(self):
        return self.cleaned_data.get('content')


class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['question',]
    def clean_question(self):
        return self.cleaned_data.get('question')
