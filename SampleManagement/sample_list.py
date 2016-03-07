from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from SampleManagement.sample import Sample


def sample_list_handler(request):
    """Transmit sample data to the frontend"""
    from SampleManagement.db.sample_db import search_all_sample
    samples = search_all_sample()
    return render_to_response(r'sample_list.html', {'data': samples}, context_instance=RequestContext(request))


def insert_list_handler(request):
    """ Get sample data to be inserted and insert them into the database"""
    from SampleManagement.db.sample_db import insert_sample
    name = request.POST['name']
    chemical = request.POST['chemical']
    notes = request.POST['notes']

    new_sample = Sample(name=name, chemical=chemical, notes=notes)

    insert_sample(new_sample)
    return HttpResponseRedirect('/sample-list/')


def open_list_modifier_handler(request):
    """Transmit sample data to the frontend"""
    is_edit = False
    passed_data = {}
    if request.POST:
        is_edit = True
        id = request.POST['id']
        name = request.POST['name']
        chemical = request.POST['chemical']
        notes = request.POST['notes']
        save_sample = {'id': id, 'name': name, 'chemical': chemical, 'notes': notes}
        passed_data = {'data': save_sample}
    passed_data['is_edit'] = is_edit
    return render_to_response(r'list_modifier.html', passed_data, context_instance=RequestContext(request))


def edit_list_handler(request):
    """ Get sample data to be edited and edit them in the database"""
    from SampleManagement.db.sample_db import edit_sample
    id = request.POST['id']
    name = request.POST['name']
    chemical = request.POST['chemical']
    notes = request.POST['notes']

    sample = Sample(id=id, name=name, chemical=chemical, notes=notes)
    edit_sample(sample)
    return HttpResponseRedirect('/sample-list/')


def cancel_handler(request):
    """ When the cancel button was pressed, redirect to sample_list template"""
    return HttpResponseRedirect('/sample-list/')
