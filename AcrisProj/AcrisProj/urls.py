"""
Definition of urls for AcrisProj.
"""
from django.conf.urls import include #added my AM
from django.contrib import admin #added my AM

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
 

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,  
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^metodologjia$', app.views.metodologjia, name='metodologjia'),
     url(r'^logged$', app.views.logged, name='logged'),
     url(r'^logged_ial$', app.views.logged_ial, name='logged_ial'),
     url(r'^logged_kv$', app.views.logged_kv, name='logged_kv'),
     url(r'^komisionet$', app.views.komisionet, name='komisionet'),
     url(r'^komisionet_create/$', app.views.komisionet_create, name='komisionet_create'),
     url(r'^(?P<komisionet_id>[0-9]+)/$', app.views.komisionet_edit, name='komisionet_edit'),
     url(r'^(?P<komisionet_id>[0-9]+)/$', app.views.komisionet_detail, name='komisionet_detail'),
]
