# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	# home page urls
	url(r'^$', 'students.views.home_page', name='home'),
	
    # Students urls
    url(r'^students/$', 'students.views.students_list', name='students'),
    url(r'^students/add/$', 'students.views.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_delete', name='students_delete'),
	
    # Groups urls
    url(r'^groups/$', 'students.views.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups_delete', name='groups_delete'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()



