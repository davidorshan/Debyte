from django.db import models
import debates
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=20)
	id = models.IntegerField(primary_key=True)

	
class Chatroom(models.Model):
	name = models.CharField(max_length=200)
	id = models.IntegerField(primary_key=True)
	starttime = models.DateTimeField()
	endtime = models.DateTimeField()

class Message(models.Model):
	timestamp = models.DateTimeField()
	user = models.ForeignKey(debates.models.User)
	message = models.CharField(max_length=500, primary_key=True)
	chatroom_id = models.ForeignKey(Chatroom)




	


