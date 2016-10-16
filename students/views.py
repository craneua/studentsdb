# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'students/home_page.html', {})
	
def students_list(request):
    return HttpResponse('<h1>Students Listing</h1>')
	
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
	
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')
	
def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
	
	
'''
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Олег',
         'last_name': u'Ячменев',
         'ticket': 2103,
         'image': 'img/avatar03.jpg'},
        {'id': 2,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 2214,
         'image': 'img/podoba.jpeg'},
        {'id': 3,
         'first_name': u'Андрій',
         'last_name': u'Іванов',
         'ticket': 2307,
         'image': 'img/avatar03.jpg'},
        )
    return render(request, 'students/students_list.html', {'students': students})

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': u'МтМ - 21',
         'leader_name': u'Олег Ячменев'},
        {'id': 2,
         'group_name': u'МтМ - 22',
         'leader_name': u'Віталій Подоба'},
        {'id': 3,
         'group_name': u'МтМ - 23',
         'leader_name': u'Андрій Іванов'},
        )
    return render(request, 'students/groups_list.html', {'groups': groups})
'''