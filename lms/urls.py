from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'library.views.home', name='home'),
    url(r'^login/$', 'library.views.sign_in', name='signin'),
    url(r'^logout/$', 'library.views.sign_out', name='signout'),
    url(r'^deo/$', 'library.views.deo_home'),
    url(r'^deo/add_book/$', 'library.views.add_book'),
    url(r'^deo/edit_book/$', 'library.views.edit_book'),
    url(r'^deo/remove_book/$', 'library.views.remove_book'),
    url(r'^deo/add_bookcategory/$', 'library.views.add_bookcategory'),
    url(r'^deo/edit_bookcategory/$', 'library.views.edit_bookcategory'),

    url(r'^staff/$', 'library.views.staff_home'),
    url(r'^staff/advance_booking/$', 'library.views.add_advancebook'),
    url(r'^staff/request-for-book/$', 'library.views.request_for_book'),

    url(r'^student/$', 'library.views.student_home'),
    url(r'^student/advance_booking/$', 'library.views.add_advancebook'),
    url(r'^student/request-for-book/$', 'library.views.request_for_book'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^librarian/$', 'library.views.librarian'),
    url(r'^librarian/receive_book/$', 'library.views.receive_book'),
    url(r'^issue/(?P<id>[0-9]+)/$', 'library.views.issue'),
    url(r'^recieved/(?P<bid>[0-9]+)/$', 'library.views.recieved'),
    url(r'^issue_book/(?P<bid>[0-9]+)/$', 'library.views.issue_book'),

    url(r'^admin/', include(admin.site.urls)),
)
