from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def checkout(request):
    return render(request, 'checkout.html')
