from unicodedata import name
from django.shortcuts import render
from django.db import models
from django.urls import reverse
from .models import Pokemon

def index(request):
    '''
    home page 
    '''
    num_pokemon = Pokemon.objects.all().count()
    type_count = Pokemon.objects.values('type1').annotate(n=models.Count('type1')).order_by('-n')

    context = {
        'num_pokemon': num_pokemon,
        'type_count': type_count,
    }
    
    return render(request, 'dex/index.html', context=context)

def typeListView(request, _type):
    '''
    view to display Pokemon having a specific primary type
    '''
    pokemon = Pokemon.objects.filter(type1=_type.capitalize())
    p_type = _type # can't use underscore var's in templates
    context = {
        'pokemon': pokemon,
        'p_type': p_type,
    }

    def get_absolute_url(self):
    
        return reverse("type_list", kwargs={'_type': self._type})
    
    return render(request, 'dex/type.html', context=context)

def pokeDetailView(request, pname):
    '''
    view to display detailed info on a particular Pokemon
    '''
    p = Pokemon.objects.get(name=pname.capitalize())

    context = {
        'p': p,
    }

    def get_absolute_url(self):
    
        return reverse("poke_detail", kwargs={'pname': self.pname})

    return render(request, 'dex/detail.html', context=context)