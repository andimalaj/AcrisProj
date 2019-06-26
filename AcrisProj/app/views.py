"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse


def in_group_IAL(user):
    return user.groups.filter(name="IAL").exists()

def in_group_KV(user):
    return user.groups.filter(name="Komisioni i Vlersimeve").exists()



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def metodologjia(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/metodologjia.html',
        {
            'title':'metodologjia',
            'message':'Metodologjia e vleresimit',
            'year':datetime.now().year,
        }
    )




@login_required
def logged(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    group = request.user.groups.filter(user=request.user)[0]

    if group.name=="IAL":
        return HttpResponseRedirect(reverse('logged_ial'))
  

    elif group.name=="Komisioni i Vlersimeve":
        #return HttpResponseRedirect(reverse('logged_kv'))
        return HttpResponseRedirect(reverse('logged_kv'))
        return render(
            request,
            'app/logged_kv.html',
            {
                'title':'ADMIN-KV',
                'message':'Faqa e menaxhimit KV',
                'year':datetime.now().year,
            }
        )
    else :
        return render(
            request,
            'app/logged.html',
            {
                'title':'Login Home',
                'message':'Faqa e menaxhimit',
                'year':datetime.now().year,
            }
        )


@login_required
@user_passes_test(in_group_IAL)
def logged_ial(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logged_ial.html',
        {
            'title':'ADMIN-IAL',
            'message':'Faqa e menaxhimit IAL',
            'year':datetime.now().year,
        }
    )

@login_required
@user_passes_test(in_group_KV)
def logged_kv(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logged_kv.html',
        {
            'title':'ADMIN-KV',
            'message':'Faqa e menaxhimit KV',
            'year':datetime.now().year,
        }
    )


