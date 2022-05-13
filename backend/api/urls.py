"""
API url patterns
"""
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^classes/$', views.class_list.as_view()),
    re_path(r'^classes/(?P<pk>[0-9]+)$', views.class_detail.as_view()),
    re_path(r'^careers/$', views.career_list.as_view()),
    re_path(r'^careers/(?P<pk>[0-9]+)$', views.career_detail.as_view()),
    re_path(r'^info/$', views.info_list.as_view()),
    re_path(r'^info/(?P<pk>[0-9]+)$', views.info_detail.as_view()),
]
