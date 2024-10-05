from django.urls import path
from model import views

urlpatterns = [
    path('',views.index,name='index'),
    path('raw',views.raw_query,name='raw'),
    path('product_form',views.product_form,name='product')
]