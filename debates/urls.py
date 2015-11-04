from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
    url(r'^create_debate$', views.create_debate, name='create_debate'),
    url(r'^created_dummy$', views.created_dummy, name='created_dummy'),
]


