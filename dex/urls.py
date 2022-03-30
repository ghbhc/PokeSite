from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/<str:_type>', views.typeListView, name='type_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
