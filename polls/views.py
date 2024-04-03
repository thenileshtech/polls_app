from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("pub_date")
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Quetion does not exist")
    return render(request, "polls/detail.html", {"question":question})

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except:
        return render(request, "polls/results.html",{"question":question,"error_message":"Request is not valid",})
    selected_choice.votes+=1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})