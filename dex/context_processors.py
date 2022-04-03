from django.db import models
from .models import Pokemon

def navTypes(request):

    types = Pokemon.objects.order_by('type1').values('type1').distinct()
    return {
        'types': types
    }
