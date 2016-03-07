from django.conf.urls import url
from SampleManagement.sample_list import *

urlpatterns = [
    url(r'^$', sample_list_handler),
    url(r'^sample-list/', sample_list_handler),
    url(r'^list-modifier/', open_list_modifier_handler),
    url(r'^insert-list/', insert_list_handler),
    url(r'^edit-list', edit_list_handler),
    url(r'^cancel', cancel_handler),
]
