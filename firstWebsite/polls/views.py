from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Question

def index(request):
	lastest_question_list = Question.objects.order_by('pub_date')[:5]
	question_names = []
	for q in lastest_question_list:
		question_names.append(q.question_text)
	output = '<br>'.join(question_names)
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)
