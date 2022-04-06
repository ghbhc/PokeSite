from unicodedata import name
from django.shortcuts import render
from django.db import models
from django.urls import reverse
from django.views.generic import ListView
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
    annoying_url_names = ['mr-mime', 'nidoran-female', 'nidoran-male', 'farfetchd']
    if pname in annoying_url_names:
        p = Pokemon.objects.get(name=pname)
    else:
        p = Pokemon.objects.get(name=pname.capitalize())

    num = p.number
    if num == 1:
        prev = Pokemon.objects.get(number=151)
    else:
        prev = Pokemon.objects.get(number=num-1)
    if num == 151:
        next = Pokemon.objects.get(number=1)
    else:
        next = Pokemon.objects.get(number=num+1)

    context = {
        'p': p,
        'prev': prev,
        'next': next,
    }

    def get_absolute_url(self):
    
        return reverse("poke_detail", kwargs={'pname': self.pname})

    return render(request, 'dex/detail.html', context=context)

def searchResultsView(request):
    '''    
    view to display search results of pokemon names
    '''
    if request.method == "POST":
        
        query = request.POST['query']
        poke_list = Pokemon.objects.filter(name__icontains=(query))

        context = {
            'query': query,
            'poke_list': poke_list
        }

        return render(request, 'dex/search_results.html', context=context) 
    else:
        context = {

        }

        return render(request, 'dex/search_results.html', context=context) 

def allView(request):
    '''
    view to display all original 151 Pokemon
    '''
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    
    return render(request, 'dex/all.html', context=context)
