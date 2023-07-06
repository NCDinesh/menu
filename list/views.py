from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):

    item_data = Item.objects.all()

    return render(request,"index.html",{'item_data':item_data})

def item(request):
    return render(request,"item.html")


def update(request):
    if request.method == "POST":
        itemname = request.POST["item-name"]
       
        itemtype = request.POST["item-category"]
        itemprice = request.POST["item-price"]
    
        item = Item.objects.create(itemname=itemname, itemtype=itemtype, itemprice= itemprice)
        item.save()
        return redirect("/")
    
    
    else :
        return redirect("/")