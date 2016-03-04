from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.utils.safestring import mark_safe
import json
from django.core import serializers

def sample_list_handler(request):
    data1 = {}
    data1[u'name'] = u'test name1'
    data1[u'chemical'] = u'test c1'
    data1[u'notes'] = u'test note1'

    data2 = {}
    data2[u'name'] = u'test name2'
    data2[u'chemical'] = u'test c2'
    data2[u'notes'] = u'test note2'

    data = {'sample_data':[data1, data2]}
    return render_to_response(r'sample_list.html', {'data':data})
