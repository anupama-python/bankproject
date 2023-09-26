from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests import auth
from .models import district,branch

# Create your views here.
def base(request):
    return render(request,"base.html")
def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')


        return render(request, "login.html")

def register(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['confirm password']
            if password == cpassword:
                return render(request,"login.html")
            if password!=cpassword:
                return render(request,"register.html")
        return render(request,"register.html")



def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phonenumber = request.POST['phone number']
        address = request.POST['address']
        district = request.POST['district']
        if username==username:
            return render(request,'form.html')
    return render(request,'form.html')
def new(request):
    pass
    return render(request,"new.html")
def message(request):
    pass
    return render(request,"message.html")
def getdata(request):
    template_name='form.html'
    districtcontext=district.objects.all()
    branchcontext=branch.objects.all()
    return render(request,template_name,{'district':districtcontext,'branch':branchcontext})