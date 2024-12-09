from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from Home.models import Contact,services
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from news.models import News
from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    # context={
    #     'variable' : "Dhruv"
    # }
    newsdata = News.objects.all()
    data = {
        'newsdata': newsdata
    }
    return render(request, 'home.html',data)
    # return render(request, 'home.html',context)
    # return HttpResponse("Hello Welcome to this world")

@login_required(login_url='login')
def newsdetail(request,id):
    # print("helllo")
    # print(id)
    newsData = News.objects.all()
    # data = {
    #     'newsData' : newsData
    # }
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request,'basic.html',context)  
 
@login_required(login_url='login')    
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def Blog(request):
    serviceData = services.objects.all().order_by('id')[:10]
    for a in serviceData:
        print(a.service_img) 
        print(a.service_info)
    # print(services)
    
    data={
        'serviceData':serviceData
        }
    
    return render(request, 'services.html',data)

@login_required(login_url='login')
def contect(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contect=Contact(name=name, email=email, phone=phone , message=message , date=datetime.today())
        contect.save()
        messages.success(request, "Your Message Has been sent")
        
    return render(request,'contect.html')

@unauthenticated_user
def signin_view(request):
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request,'Accout is created.')
                return redirect('login')
            else:
               context = {'form':form}
               messages.info(request,'Invalid creadentials')
               return render(request,'signin.html',context)
        
        context = {'form':form}
        return render(request,'signin.html',context)

@unauthenticated_user
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username},You are logged in.')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
        
    return render(request, 'login.html')

@login_required(login_url='login')
def Profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def logout_view(request):
    username = request.user.username
    logout(request)
    messages.info(request, f'{username} logged out successfully')
    return redirect('/')
