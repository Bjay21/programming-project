from django.conf import settings
from django.conf.urls import url

from youtube import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]