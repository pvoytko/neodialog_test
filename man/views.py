# -*- coding: utf-8 -*-

from django.http import HttpResponse

def home(request):
    res = u"OK"
    return HttpResponse(res)