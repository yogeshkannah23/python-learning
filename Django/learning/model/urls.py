from django.urls import path
from model import views

urlpatterns = [
    path('',views.index,name='index'),
    path('raw',views.raw_query,name='raw')
]