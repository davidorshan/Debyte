from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Debate, Category, ChatMessage
from django.http import Http404

# Create your views here.

def front_page(request, redirect_message=None):

    categories = Category.objects.all()
    #return HttpResponse(','.join([a.topic for a in categories[1].debate_set.all()]))
    context = {"categories":categories, "redirect_message":redirect_message}
    print context
    return render(request, "front.html", context)

def join_debate(request, debateId=-1):
    try:
        debate = Debate.objects.get(pk=debateId)
    except Question.DoesNotExist:
        raise Http404("Debate does not exist")
    if debate.status == 1:
        #concurrency issues
        return front_page(request, redirect_message="Someone already joined that debate! Sorry")
    if not request.POST:
        #if need to make name
        request.session[str(debateId)] = "TMP"
        context = {"debateId":debateId}
        return render(request, "join_debate.html", context)
    request.session[str(debateId)] = request.POST["name"]
    debate.status = 1
    debate.save()
    #TODO add debate
    #todo add page that says sorry
    #return front_page(request, redirect_message="JoinedDebate!")
    return detail(request, debateId)

def detail(request, chatroom_id):
    chatroom = get_object_or_404(Debate, pk=chatroom_id)
    messages = ChatMessage.objects.filter(debate=chatroom.id)
    #TODO sort by timestamp
    print request.session.keys()
    return render(request, "chatroom.html", {'chatroom':chatroom, 'messages':messages, 'username':request.session[str(chatroom_id)]})	
	
def create_debate(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, 'create_debate.html', context)

def add_message(request, debateId):
	#TODO security! Keep track of username!
    new_message = ChatMessage()
    new_message.message = request.POST['message']
    new_message.user = request.session[str(debateId)]
    new_message.debate = Debate.objects.get(pk=debateId)
    new_message.save()
    return detail(request, debateId)
	
def created_dummy(request):
    new_debate = Debate()
    new_debate.topic = request.POST['topic']
    new_debate.orig_position = request.POST['position']
    new_debate.anon_username_starter = request.POST["starter_name"]
    #deal with joining multiple debates later
    #TODO add user
    #new_debate.anon_username_starter = request.POST['starter_name']
    new_debate.category = Category.objects.get(pk=request.POST['category'])
    new_debate.allow_anon_users = 1            #defaulted to true for now
    new_debate.save()
    request.session[str(new_debate.pk)] = request.POST["starter_name"]
    print new_debate.pk
    #TODO redirect to debate page
    #return render(request, 'created_dummy.html')
    return detail(request, new_debate.pk)
