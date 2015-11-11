from django.contrib import admin

# Register your models here.

from .models import Debate, Category, User

admin.site.register(Debate)
admin.site.register(Category)
admin.site.register(User)
