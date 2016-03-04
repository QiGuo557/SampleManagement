from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
import json
from django.core import serializers
from sample_form import SampleForm

def sample_list_handler(request):
    # TODO read from DB
    data1 = {}
    data1[u'name'] = u'test name1'
    data1[u'chemical'] = u'test c1'
    data1[u'notes'] = u'test note1'

    data2 = {}
    data2[u'name'] = u'test name2'
    data2[u'chemical'] = u'test c2'
    data2[u'notes'] = u'test note2'

    data = {'sample_data':[data1, data2]}
    return render_to_response(r'sample_list.html', {'data':data},  context_instance=RequestContext(request))

def open_save_list_handler(request):
    return render_to_response(r'list_modifier.html', None ,context_instance=RequestContext(request))

def open_sample_list_handler(request):
    print request.POST['name']
    print request.POST['chemical']
    print request.POST['notes']

    # TODO Save to DB
    # TODO Call sample_list_handler
    # return render_to_response(r'sample_list.html', None ,context_instance=RequestContext(request))

def edit_sample_handler(request):
    # TODO
    pass