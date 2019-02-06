# -*- coding: utf-8  -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
from crdist.models import District

class Test(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    province = models.ForeignKey(District, related_name="prov", on_delete=models.CASCADE)

