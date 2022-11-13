from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from ejeevanprateek.models import Contact, Parameter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.models import Account
from accounts.form import SigninForm
from ejeevanprateek.form import ContactForm, ParameterForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent.')
    context = {"form":form}
    return render(request, 'contact.html', context)

def patient_data(request):
    if request.method == "GET":
        aadhaar_no = request.GET.get("aadhaar_no")
        patient_name = request.GET.get("patient_name")
        if aadhaar_no == "all" or patient_name == "all":
            users = Parameter.objects.all()
        else:
            users = Parameter.objects.filter(patient_name=patient_name).filter(aadhaar_no=aadhaar_no)
            patient_info = {
                'users':users,
            }
            return render(request, "patient_info.html", patient_info)

def services(request):
    return render(request,"services.html")

def customer_signin(request):
    return render(request, "customer_signin.html")

def customer_login(request):
    return render(request, "customer_login.html")

def handlesignin(request):
    pass

def handlelogin(request):
    pass

def handlelogout():
    logout(request)
    messages.success(request, "Successfully Logged Out")
