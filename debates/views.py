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
