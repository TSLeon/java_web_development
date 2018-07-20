from django.db import models

# Create your models here
class Question(models.Model):
    question_id    = models.IntegerField(primary_key=True,default=1)
    question_text  = models.CharField(max_length=200)
    option_one     = models.CharField(max_length=100,default='not')
    option_twe     = models.CharField(max_length=100,default='not')
    option_three   = models.CharField(max_length=100,default='not')
    option_four    = models.CharField(max_length=100,default='not')
    answer         = models.CharField(max_length=2,default='A')


class Result(models.Model):
    user  = models.CharField(max_length=200)
    score = models.IntegerField()
    time  = models.CharField(max_length=25)