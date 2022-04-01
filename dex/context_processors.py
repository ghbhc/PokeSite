from .models import Pokemon

def navTypes(request):

    types = Pokemon.objects.order_by().values('type1').distinct()
    return {
        'types': types
    }