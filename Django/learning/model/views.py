from django.shortcuts import render
from django.http import request,HttpResponse
from model.models import *
# Create your views here.



def index(request):
    return HttpResponse("Hi yogesh")

def raw_query(request):
    shirts = Shirt.objects.raw("select * from model_shirt where shirt_size='M' ")
    print(shirts[0].name)
    return HttpResponse(shirts[0].name)
