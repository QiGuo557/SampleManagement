from django import forms

class SampleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    chemical = forms.CharField(label="Chemical", max_length=100)
    notes = forms.CharField(label="Notes", max_length=100)