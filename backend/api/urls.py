"""
API url patterns
"""
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("hello", views.hello_world),
    re_path(r'^classes/$', views.class_list.as_view()),
    re_path(r'^classes/(?P<pk>[0-9]+)$', views.class_detail.as_view()),
]
