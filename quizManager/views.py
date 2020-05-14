from django.shortcuts import render
from django.http import HttpResponse
from  quizManager.models import Question

def index(request):
    question = Question.objects.first()
    return render(request, 'quizManager/question.html', {'question': question})



