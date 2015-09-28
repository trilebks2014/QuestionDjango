from polls.models import Question,Choice
from django.template import RequestContext,loader
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# def IndexView(generic.ListView):
# 	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	# context = RequestContext(request, {
# 	# 	'latest_question_list': latest_question_list,
# 	# })
# 	template_name='polls/index.html'
# 	context_object_name='lastest_question_list'

# 	def get_queryset(self):
# 		"""Return the last five published questions."""
# 		return Question.objects.order_by(-pub_date)[:5]
# 	# context = {'latest_question_list': latest_question_list}
# 	# return render(request, 'polls/index.html', context)
# 	# return HttpResponse(template.render(context))
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		# return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# def DetailView(request, question_id):
# 	# lasted_choice_list = Choice.objects.order_by()
# 	try:
# 		question=Question.objects.get(pk=question_id)
# 	except Question.DoesNotExit:
# 		raise  Http404("Question does no exist")
# 	return render(request,'polls/detail.html',{'question':question})
	# return HttpResponse("You're looking at question %s." % question_id)
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

# def ResultsView(request, question_id):
#  	question = get_object_or_404(Question, pk=question_id)
# 	return render(request,'polls/results.html',{'question':question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('results', args=(p.id,)))

# class vote(generic.DetailView):
# 	model=Question
# 	template_name='polls/results.html'
