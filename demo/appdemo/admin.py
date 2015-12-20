from django.contrib import admin

# Register your models here.
from crdist.widgets import DistrictSelect
from .models import Test
from django import forms

class TestAdminForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        widgets = {
          'district': DistrictSelect(attrs={"class": "form-control"}),
          'province': DistrictSelect(),
        }


class TestAdmin(admin.ModelAdmin):
    form = TestAdminForm

admin.site.register(Test, TestAdmin)
