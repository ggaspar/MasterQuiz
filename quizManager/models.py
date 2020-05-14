from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_response = models.CharField(max_length=50)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)