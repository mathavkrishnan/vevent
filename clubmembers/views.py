from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import eventsform
from .models import events,user
# Create your views here.
@login_required
def home(request):
    if request.method == 'GET':
        eventz = events.objects.order_by("eventdate")
        name = user.objects.filter(username = request.user)
        return render(request,'clubmembers/home.html',{'forms':eventsform,'events':eventz})
    else:
        form = eventsform(request.POST, request.FILES)
        newevent = form.save(commit=False)
        newevent.user = request.user
        newevent.save()
        return redirect('home')
def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_student:
            login(request,user)
            return redirect('home')
    return render(request,'clubmembers/login.html',{'form':form})
def yourevents(request):
    if request.method == 'POST':
        events.objects.filter(link = request.POST['newfinder']).delete()
        forms = eventsform(request.POST)
        newevent = forms.save(commit=False)
        newevent.user = request.user
        newevent.save()
        return redirect('home')
    else:
        myevents = events.objects.filter(user = request.user)
        return render(request,'clubmembers/yourevents.html',{'regev':myevents,'forms':eventsform})
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
def deleteevent(request):
    if request.method == 'POST':
        events.objects.filter(link = request.POST['finder']).delete()
        return redirect('yourevents')
def searchelement(request):
    if request.method == 'POST':
        results = events.objects.filter(eventname = request.POST.get('searched'))
        return render(request,'clubmembers/home.html',{'events':results}) 


