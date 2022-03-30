from django.shortcuts import render
from django.db import models
from django.views import generic
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
    type_list = Pokemon.objects.filter(type1=_type.capitalize())
    context = {
        'type_list': type_list,
    }
    
    return render(request, 'dex/type.html', context=context)
