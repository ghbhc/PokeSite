from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/<str:_type>', views.typeListView, name='type_list'),
]
