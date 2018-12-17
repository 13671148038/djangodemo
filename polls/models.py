from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')


class Choice(models.Model):
    question_id = models.IntegerField(max_length=11)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
