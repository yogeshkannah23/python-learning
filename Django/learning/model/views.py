from django.shortcuts import render
from django.http import request,HttpResponse
from model.models import *
from model.forms import ProductForm
from django.db import transaction
# Create your views here.



def index(request):
    return HttpResponse("Hi yogesh")

def raw_query(request):
    shirts = Shirt.objects.raw("select * from model_shirt where shirt_size='M' ")
    print(shirts[0].name)
    return HttpResponse(shirts[0].name)


#                                                        Transaction Example
def product_form(request):

    if request.method == 'POST':
        form =  ProductForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                print(form.cleaned_data)
                Product.objects.filter(name="Keyboard").update(quantity= (Product.objects.filter(name="Keyboard")[0].quantity - order.quantity))
                transaction.on_commit(send_mail)
        else:
            form = ProductForm()
            return render(request,'index.html',{'form':form})
        
    form = ProductForm()
    return render(request,'index.html',{'form':form})

def send_mail():
    print(f"Email sent to ")