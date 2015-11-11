from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Chatroom, User, Message
# Create your views here.
def index(request):
	latest_chatrooms_list = Chatroom.objects.order_by('-id')[:5]
	context = {'latest_chatrooms_list': latest_chatrooms_list,}
	return render(request, 'chat/index.html', context)
	
def detail(request, chatroom_id):
	chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
	messages = Message.objects.filter(chatroom_id=chatroom.id)
	return render(request, "chat/detail.html", {'chatroom':chatroom, 'messages':messages})