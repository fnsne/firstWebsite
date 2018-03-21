from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Question
from django.template import loader

def index(request):
	lastest_question_list = Question.objects.order_by('pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'lastest_question_list': lastest_question_list
	}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)
