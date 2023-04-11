from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
from .models import indexmail,detailmail1
from .forms import FormContactForm,FormContact
# Create your views here.
def index(request):
    if request.method=="POST":
        email=request.POST.get("email")
        index=indexmail(email=email)
        index.save()
        
    return render(request,"index.html")
    
def indexdetail1(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email1=request.POST.get("email1")
        date=request.POST.get("date")
        time=request.POST.get("time")
        people=request.POST.get("people")
        indexdetail=detailmail1(name==name,email1==email1,date==date,time==time,people==people)
        indexdetail.save()
    return render(request,"index.html")  
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def menu(request):
    return render(request,"menu.html")
def reservation(request):
    return render(request,"reservation.html")
def service(request):
    return render(request,"service.html")
def testimonial(request):
    return render(request,"testimonial.html")

