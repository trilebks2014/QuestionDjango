from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question,Choice
from django.template import RequestContext,loader
from django.http import Http404

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ', '.join([p.question_text for p in latest_question_list])
	template = loader.get_template('polls/index.html')
	# context = RequestContext(request, {
	# 	'latest_question_list': latest_question_list,
	# })
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	# return HttpResponse(template.render(context))
def detail(request, question_id):
	# lasted_choice_list = Choice.objects.order_by()
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExit:
		raise  Http404("Question does no exist")
	return render(request,'polls/detail.html',{'question':question})
	# return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)