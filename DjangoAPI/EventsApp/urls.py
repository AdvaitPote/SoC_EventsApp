from django.urls import re_path
from EventsApp import views

urlpatterns=[
    re_path(r'^event/$', views.eventApi),
    re_path(r'^event/([0-9]+)$', views.eventApi)
]