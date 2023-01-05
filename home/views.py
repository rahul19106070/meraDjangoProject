from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
# from django.contrib.messages import constants as messages
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        "variable1":"this is rahul",
        "variable2": "this is prince"
    }
    return render(request,'index.html',context)
    # messages.success(request,"this is a test message")

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent')


    return render(request,'contact.html')
    # return HttpResponse("this is contact page")
