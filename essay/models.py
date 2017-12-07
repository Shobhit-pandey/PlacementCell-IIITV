from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from quiz.get_username import get_username
from quiz.models import Question
from django.db import models


@python_2_unicode_compatible
class Essay_Question(Question):
    user_id = models.CharField(default=get_username(), max_length=100, null=False, blank=False, editable=False)

    def check_if_correct(self, guess):
        return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay style question")
        verbose_name_plural = _("Essay style questions")