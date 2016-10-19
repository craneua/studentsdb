# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups
def journals_list(request):
    return render(request, 'students/journals_list.html')
