import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):  # Class Question :
    # Text of the question and publication date
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Change print format
    def __str__(self):
        return self.question_text
        # https://stackoverflow.com/questions/39883950/str-returned-non-string-type-tuple
        # No es util en los tests
        # return 'Question: {} -- Publication date: {}'.format(self.question_text, self.pub_date)

    # Method: Published recently
    def was_published_recently(self):
        # With Bug:
        # El dia antes o cualquier fecha mayor a la de hoy
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # Without bug:
        # El dia antes o el mismo dia
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # Allow sort in admin site
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):  # Class Chocie :
    # Text of the choice and a vote tally
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Change print format
    def __str__(self):
        return self.choice_text
        # No es util en los tests
        # return 'Choice: {} -- Votes: {}'.format(self.choice_text, self.votes)
