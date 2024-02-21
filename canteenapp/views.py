

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from canteenapp.models import users,orders
gname="User"
# Create your views here.
def index(request):
    prices={"Wada Paav":12,"Idli Chatni":25,"Dosa":20,"Frooti":10,"Amul lassi":15,"Samosa":12,"Misal Pav":20,"Kachori":10}
    if request.method == "POST":
        name = request.POST.get("name")
        mobileno = request.POST.get("mobile_number")
        fooditem = request.POST.get("menu")
        quantity = request.POST.get("quantity")
        price=prices[fooditem]*int(quantity)
        print(name,mobileno,fooditem,quantity,price)
        ord=orders(name=name,mobileno=mobileno,fooditem=fooditem,quantity=quantity,price=price)
        ord.save()
    #orders.objects.all().delete()
    #print(qw[0].name,qw[0].fooditem,qw[0].price)
    return render(request,"index.html")

def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

def galary(request):
    return render(request,"galary.html")

def database(request):
    qw = orders.objects.all()
    context = {"objlist": qw, "Username": gname}
    return render(request,"database.html",context)