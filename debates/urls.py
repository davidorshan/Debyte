from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
    url(r'^create_debate$', views.create_debate, name='create_debate'),
    url(r'^created_dummy$', views.created_dummy, name='created_dummy'),
    url(r'^(?P<debateId>[0-9]+)/add_message$', views.add_message, name='add_message'),
    url(r'^(?P<debateId>[0-9]+)/join/$', views.join_debate, name='join_debate'),
	url(r'^(?P<chatroom_id>[0-9]+)/$', views.detail, name='chatroom')
]


