from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

# Create your models here.
from froala_editor.fields import FroalaField


class Share(models.Model):
    current_datetime = datetime.now()
    question = FroalaField(theme='dark', )
    timestamp = models.DateTimeField(default=current_datetime)
    user = models.ForeignKey(User, default="0")

    def __init__(self, *args, **kwargs):
        super(Share, self).__init__(*args, **kwargs)
        self.current_datetime = datetime.now()

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('mywebsite:student')


class ShareReply(models.Model):
    content = FroalaField(theme='dark')
    timestamp = models.DateTimeField(default=datetime.now())
    share = models.ForeignKey(Share, default="ss")
    user = models.ForeignKey(User, default="0")

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('mywebsite:student')
