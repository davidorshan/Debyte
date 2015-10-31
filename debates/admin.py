from django.contrib import admin

# Register your models here.

from .models import Debate, Category

admin.site.register(Debate)
admin.site.register(Category)
