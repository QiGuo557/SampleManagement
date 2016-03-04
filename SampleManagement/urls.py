from django.conf.urls import url
from django.contrib import admin
from SampleManagement.sample_list import sample_list_handler
from SampleManagement.list_modifier import list_modifier
urlpatterns = [
    url(r'^sample-list/', sample_list_handler),
    url(r'^list-modifier/', list_modifier),
]
