from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
    url(r'^create_debate$', views.create_debate, name='create_debate'),
    url(r'^(?P<debateId>[0-9]+)/waiting$', views.waiting, name='waiting'),
	url(r'^(?P<debateId>[0-9]+)/waiting_done$', views.waiting_done, name='waiting_done'),
    url(r'^(?P<debateId>[0-9]+)/add_message$', views.add_message, name='add_message'),
    url(r'^(?P<debateId>[0-9]+)/join/$', views.join_debate, name='join_debate'),
    url(r'^(?P<chatroom_id>[0-9]+)/$', views.detail, name='chatroom'),
    url(r'^(?P<chatroom_id>[0-9]+)/username$', views.get_username, name='get_username'),
    url(r'^(?P<chatroom_id>[0-9]+)/chat_refresh$', views.chat_refresh),
]
