from django.shortcuts import render
from django.db import models
from .models import Pokemon

# Create your views here.

def index(request):
    num_pokemon = Pokemon.objects.all().count()
    type_count = Pokemon.objects.values('type1').annotate(n=models.Count('type1')).order_by('-n')

    context = {
        'num_pokemon': num_pokemon,
        'type_count': type_count,
    }
    
    return render(request, 'dex/index.html', context=context)
