"""
Definition of views.
"""

from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

#from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required,user_passes_test

#from django.contrib.auth.decorators import user_passes_test
#from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from .models import Komisionet

from .forms import KomisionetForm


#from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

@login_required
@user_passes_test(in_group_KV)
def komisionet(request):
    """Renders the about page."""
    #assert isinstance(request, HttpRequest)
    all_komisionet = Komisionet.objects.all()
    template = loader.get_template('app/komisionet.html')
    context = { 'all_komisionet' : all_komisionet,
               'title':'Komisionet',
            'message':'Komisionet e Vlersimit',
            'year':datetime.now().year,
        }

    return HttpResponse( template.render(context,request))

@login_required
@user_passes_test(in_group_KV)
def komisionet_create(request):
    if not request.user.is_authenticated():
        return render(request, 'app/login.html')
    else:
        form = KomisionetForm(request.POST or None)
        if form.is_valid():
            komisionet = form.save(commit=False)
            #komisionet.emertimi = request.emertimi
            #komisionet.aktiv = request.aktiv
            komisionet.save()
            #all_komisionet = Komisionet.objects.all()
            #return render(request, 'app/komisionet.html', {'all_komisionet': all_komisionet})
            return HttpResponseRedirect(reverse('komisionet'))
        context = {
            "form": form,
        }
        return render(request, 'app/komisionet_create.html', context)
    
@login_required
def komisionet_detail(request, komisionet_id):
    user = request.user
    komisionet = get_object_or_404(Komisionet, pk=komisionet_id)
    return render(request, 'app/komisionet_detail.html', {'komisionet': komisionet})


@login_required
def komisionet_edit(request, komisionet_id):
    komisionet = get_object_or_404(Komisionet, pk=komisionet_id)    
    form = KomisionetForm(request.POST or None, instance=komisionet)
    if request.POST and form.is_valid():
        komisionet = form.save(commit=False)
        komisionet.save()
        # Save was successful, so redirect to another page
        return render(request, 'app/komisionet_detail.html', {'komisionet': komisionet})

    return render(request, 'app/komisionet_edit.html', {
        'form': form
    })