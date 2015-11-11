from django.contrib import admin

# Register your models here.
from .models import Chatroom, Message
import debates

class MessageInline(admin.StackedInline):
	model = Message


class ChatroomAdmin(admin.ModelAdmin):
	inlines = [MessageInline]

admin.site.register(Chatroom, ChatroomAdmin)