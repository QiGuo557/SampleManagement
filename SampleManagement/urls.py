from django.conf.urls import url
from django.contrib import admin
from SampleManagement.sample_list import sample_list_handler, open_save_list_handler,open_sample_list_handler

urlpatterns = [
    url(r'^sample-list/', sample_list_handler),
    url(r'^save-list/', open_save_list_handler),
    url(r'^update-list', open_sample_list_handler),
]
