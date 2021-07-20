from django.shortcuts import render
from  .models import Order

# Create your views here.
def index(request):
    return render(request, 'index.html')


def checkout(request):

    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        location = request.POST.get('location',"")
        address = request.POST.get('address',"")
        Phone = request.POST.get('Phone',"")
        quanity = request.POST.get('quantity',"")
        totalp = request.POST.get('totalp',"")

        order = Order(name=name,email=email,location=location,address=address,Phone=Phone, quantity=quanity, totalp=totalp)
        order.save()

    return render(request, 'checkout.html')
