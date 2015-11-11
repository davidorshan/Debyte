from django.shortcuts import render
#from django.http import HttpResponse
from .models import Debate, Category

# Create your views here.

def front_page(request):

    categories = Category.objects.all()
    #return HttpResponse(','.join([a.topic for a in categories[1].debate_set.all()]))
    context = {"categories":categories}
    print context
    return render(request, "front.html", context)


def create_debate(request):

    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, 'create_debate.html', context)


def created_dummy(request):

    new_debate = Debate()
    new_debate.topic = request.POST['topic']
    new_debate.orig_position = request.POST['position']
    new_debate.category = Category.objects.get(pk=request.POST['category'])
    new_debate.allow_anon_users = 0            #defaulted to false for now
    new_debate.save()

    return render(request, 'created_dummy.html')
