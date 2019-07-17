"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .models import Komisionet,Vlersues, KomisionetV,ScopusKatalog
from django.contrib.auth.models import User

from django.forms.models import inlineformset_factory

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class KomisionetForm(forms.ModelForm):

    class Meta:
        model = Komisionet
        fields = ['emertimi', 'aktiv']

class VlersuesitForm(forms.ModelForm):

    class Meta:
        model = Vlersues
        fields = ['userid', 'aktiv']

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class KomisionetVForm(forms.ModelForm):

    class Meta:
        model = KomisionetV

        #komisioniV = forms.ModelChoiceField(queryset = Komisionet.objects.all().order_by('-emertimi') )
        #vlersuesiV = forms.ModelChoiceField(queryset = Vlersues.objects.all().order_by('userid') )
        fields = [ 'komisioni','vlersuesi']


class ScopusKatalogForm(forms.ModelForm):

    class Meta:
        model = ScopusKatalog
        fields = ['scopusid', 'pubmedid','author','affiliation','citation_count','title','issn','date','journal']