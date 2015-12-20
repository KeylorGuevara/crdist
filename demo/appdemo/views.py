# -*- coding: utf-8  -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from crdist.widgets import DistrictSelect
from crdist.models import District
from django import forms

class CRForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(),
                                  widget=DistrictSelect(attrs={"class": "form-control"}),
                                  label="Localización ")


def view_test_form(request):
    message = ""
    if request.method == 'POST':
        form = CRForm(request.POST)
        if form.is_valid():
            message= "VALID"
    else:
        form = CRForm()
    return render(request, 'appdemo/form_ejemplo.html', {'form': form, 
                                                        "message": message})
