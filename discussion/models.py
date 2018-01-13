from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

# Create your models here.
class Share(models.Model):
    question = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User,default="0")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('mywebsite:student')



class ShareReply(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=datetime.now())
    share = models.ForeignKey(Share,default="ss")
    user = models.ForeignKey(User,default="0")

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('mywebsite:student')