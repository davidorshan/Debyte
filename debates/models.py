from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
		
class User(models.Model):
    name = models.CharField(max_length=100)

class Debate(models.Model):
    topic = models.CharField(max_length=500)
    orig_position = models.CharField(max_length=500)
    starter_user = models.ForeignKey(User, related_name="debate_starter_user", default=None, blank=True, null=True)
    joiner_user = models.ForeignKey(User, related_name="debate_joiner_user", default=None, blank=True, null=True)
    status = models.IntegerField(default=0)
    anon_username_starter = models.CharField(max_length=100, default=None, blank=True, null=True)
    anon_username_joiner = models.CharField(max_length=100, default=None, blank=True, null=True)
    category = models.ForeignKey(Category)
    allow_anon_users = models.BooleanField()
    def __str__(self):
        return self.topic

class ChatMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100,default=None, blank=True, null=True)
    message = models.TextField()
    debate = models.ForeignKey(Debate)
    numberMessage = models.IntegerField(default=0)
