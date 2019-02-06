'''
Created on 16/12/2015

@author: luisza
'''


from django.conf.urls import  url
from appdemo.views import view_test_form


urlpatterns = [ url('^test$', view_test_form) ]
