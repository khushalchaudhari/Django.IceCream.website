from django.shortcuts import render, HttpResponse 
from datetime import datetime 
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

    # return HttpResponse("This is homepage")
def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def servicesiceCream (request):
    return render(request,'servicesiceCream.html')

def servicessofty(request):
    return render(request,'servicessofty.html')

def servicesfamilyPack(request):
    return render(request,'servicesicefamilyPack.html')

def contact(request):
    if request.method == "POST":
       name = request.POST.get('name')    
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       feedback = request.POST.get('feedback')
       contact = Contact(name=name, email=email, phone=phone, feedback=feedback, date = datetime.today())
       contact.save
       messages.success(request, "message sent")
    return render(request,'contact.html')
    # return HttpResponse("This is contact page")