from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import regform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from clubmembers.models import events,user
from .models import regevents
from django.contrib.auth import get_user_model
User = get_user_model()
def homies(request):
    if request.method == 'GET':
        eventz = events.objects.order_by("eventdate")
        return render(request,'nonclubmembers/home.html',{'events':eventz})
    else:
        regevents.objects.create(user = request.POST['user'],eventname = request.POST['eventname'],link = request.POST['link'],eventdate = request.POST['eventdate'],time = request.POST['time'],location = request.POST['location'])
        return redirect('registered')
def studentlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_club:
            login(request,user)
            return redirect('homies')
    return render(request,'nonclubmembers/login.html',{'form':form})
def registered(request):
    if request.method == 'GET':
        eventreg = regevents.objects.filter(user = request.user)
        return render(request,'nonclubmembers/registered.html',{'eve':eventreg})
    else:
        regevents.objects.filter(user = request.POST['user'],link = request.POST['link']).delete()
        return redirect('registered')
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
def searchelement(request):
    if request.method == 'POST':
        eventz = events.objects.order_by("eventdate")
        results = events.objects.filter(eventname = request.POST.get('searched'))
        return render(request,'nonclubmembers/home.html',{'events':eventz}) 
def signupuser(request):
    if request.method == "GET":
        return render(request,'nonclubmembers/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'],password = request.POST['password1'])
            user.save()
            return redirect('login')


