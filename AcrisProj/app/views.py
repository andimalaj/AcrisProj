"""
Definition of views.
"""

import requests
import json

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
from .models import Komisionet,Vlersues,User,KomisionetV,ScopusKatalog
from .forms import KomisionetForm,VlersuesitForm, UserForm, KomisionetVForm,ScopusKatalogForm


#from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.decorators.csrf import csrf_protect


def in_group_IAL(user):
    return user.groups.filter(name="IAL").exists()

def in_group_KV(user):
    return user.groups.filter(name="Komisioni i Vlersimeve").exists()



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    form = ScopusKatalogForm(request.POST or None)
    
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            "form": form,
        },

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
        return HttpResponseRedirect(reverse('scopus_create'))
  

    elif group.name=="Komisioni i Vlersimeve":
        #return HttpResponseRedirect(reverse('logged_kv'))
        return HttpResponseRedirect(reverse('scopus_create'))
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
   

    try :
       #komisionetV = get_object_or_404(KomisionetV, komisioni = komisionet_id)
       komisionetV = KomisionetV.objects.filter(komisioni = komisionet_id)
       #komisionetV = KomisionetV.objects.get(komisioni=komisionet_id).values()
    except Exception :
        komisionetV = None

        
    return render(request, 'app/komisionet_detail.html', {'komisionet': komisionet, 'komisionetV': komisionetV  })


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

@login_required
@user_passes_test(in_group_KV)
def vlersuesit(request):
    """Renders the about page."""
    #assert isinstance(request, HttpRequest)
    all_vlersuesit = Vlersues.objects.all()
    template = loader.get_template('app/vlersuesit.html')
    context = { 'all_vlersuesit' : all_vlersuesit,
               'title':'Vlersuesit',
            'message':'Lista e Vlersuesve',
            'year':datetime.now().year,
        }

    return HttpResponse( template.render(context,request))

@login_required
@user_passes_test(in_group_KV)
def vlersuesit_create(request):
    if not request.user.is_authenticated():
        return render(request, 'app/login.html')
    else:
        form = VlersuesitForm(request.POST or None)
        #formU = UserForm(request.POST or None)

        if form.is_valid():
            vlersuesit = form.save(commit=False)
            #komisionet.emertimi = request.emertimi
            #komisionet.aktiv = request.aktiv
            vlersuesit.save()
            #all_komisionet = Komisionet.objects.all()
            #return render(request, 'app/komisionet.html', {'all_komisionet': all_komisionet})
            return HttpResponseRedirect(reverse('vlersuesit'))
        context = {
            "form": form,
            #"formU" : formU,
        }
        return render(request, 'app/vlersuesit_create.html', context)



@login_required
@user_passes_test(in_group_KV)
def komisionetV_add(request,komisionet_id):
    if not request.user.is_authenticated():
        return render(request, 'app/login.html')
    else:
        form = KomisionetVForm(request.POST or None)
        #formU = UserForm(request.POST or None)

        if form.is_valid():
            vlersuesit = form.save(commit=False)
            #komisionet.emertimi = request.emertimi
            #komisionet.aktiv = request.aktiv
            vlersuesit.save()
            #all_komisionet = Komisionet.objects.all()
            #return render(request, 'app/komisionet.html', {'all_komisionet': all_komisionet})
            return HttpResponseRedirect(reverse('komisionet'))
        context = {
            "form": form,
            #"formU" : formU,
        }
        return render(request, 'app/komisionetV_add.html', context)



@login_required
@user_passes_test(in_group_KV)
def scopus(request):
    """Renders the about page."""
    #assert isinstance(request, HttpRequest)
    all_scopusKatalogs = ScopusKatalog.objects.all()
    template = loader.get_template('app/scopus.html')
    context = { 'all_scopusKatalogs' : all_scopusKatalogs,
               'title':'Scopus',
            'message':'Kataloget nga Scopus',
            'year':datetime.now().year,
        }

    return HttpResponse( template.render(context,request))


@login_required
@user_passes_test(in_group_KV)
#@csrf_protect
def scopus_create(request):
    if not request.user.is_authenticated():
        return render(request, 'app/login.html')
    else:
        form = ScopusKatalogForm(request.POST or None)
        if form.is_valid():
            kataloget = form.save(commit=False)
            #komisionet.emertimi = request.emertimi
            #komisionet.aktiv = request.aktiv
            kataloget.save()
            #all_komisionet = Komisionet.objects.all()
            #return render(request, 'app/komisionet.html', {'all_komisionet': all_komisionet})
            return HttpResponseRedirect(reverse('scopus'))
        context = {
            "form": form,
        }
        return render(request, 'app/scopus_create.html', context)

#@login_required
#@user_passes_test(in_group_KV)
#@csrf_protect
#def scopus_citation(request,**kwargs):
def scopus_citation(request):
    #form = ScopusKatalogForm(request.POST or None)
    #pubmedid = request.GET['pubmedid'] 
    scopusid = request.GET['scopusid'] 
    #url = "https://api.elsevier.com/content/search/scopus?query=PMID(" + pubmedid + ")&field=citedby-count" 
    url = "http://api.elsevier.com/content/search/scopus?query=SCOPUS-ID(" + scopusid + ")&field=affiliation,title,citedby-count,doi,pubmed-id,coverDate,publicationName,isbn,issn,volume,aggregationType,subtype,subtypeDescription,creator,author" 
    headers = {'X-ELS-APIKey': '7ada9ef4ce70ab99b0d4d699eb27085a'}
    p = requests.get(url,headers = headers)
   # res = p.json()
    cit_count = p.json()['search-results']['entry'][0]['citedby-count']
    pubmedid = p.json()['search-results']['entry'][0]['pubmed-id']
    author = p.json()['search-results']['entry'][0]['dc:creator']
    title = p.json()['search-results']['entry'][0]['dc:title']
    issn = p.json()['search-results']['entry'][0]['prism:issn']
    journal = p.json()['search-results']['entry'][0]['prism:publicationName']
    date = p.json()['search-results']['entry'][0]['prism:coverDate']
    affiliation = p.json()['search-results']['entry'][0]['affiliation'][0]['affilname']

    url = "http://api.elsevier.com/content/serial/title?issn=" + issn +"&view=STANDARD"
    m = requests.get(url,headers = headers)
    snip = m.json()['serial-metadata-response']['entry'][0]['SNIPList']['SNIP'][0]['$']
    sjr = m.json()['serial-metadata-response']['entry'][0]['SJRList']['SJR'][0]['$']
    citescore = m.json()['serial-metadata-response']['entry'][0]['citeScoreYearInfoList']['citeScoreCurrentMetric']



    context = {
            #"form": form,
            "cit_count": cit_count,
            "pubmedid": pubmedid,
            "author": author,
            "title": title,
            "issn": issn,
            "journal": journal,
            "date": date,
            "affiliation": affiliation,

            }
    #return render(request, 'app/scopus_create.html', context)
    response_data = {}
    response_data['cit_count'] = cit_count
    response_data['pubmedid'] = pubmedid
    response_data['author'] = author
    response_data['title'] = title
    response_data['issn'] = issn
    response_data['journal'] = journal
    response_data['date'] = date
    response_data['affiliation'] = affiliation
    response_data['snip'] = snip
    response_data['sjr'] = sjr
    response_data['citescore'] = citescore

    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json")

        

