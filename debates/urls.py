from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
]


