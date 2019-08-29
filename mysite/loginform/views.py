from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
	count =User.objects.count()
	return render(request,'home.html',{
		'count':count
		})

def bot(request):
	
	return render(request,'bot.html')

def hexa(request):
	
	return render(request,'hexa.html')

def chain(request):
	
	return render(request,'chain.html')

def pro(request):
	
	return render(request,'pro.html')

def dw(request):
	
	return render(request,'dw.html')
def deposit(request):
	
	return render(request,'deposit.html')
def withdraw(request):
	
	return render(request,'withdraw.html')

def trade(request):

	return render(request,'trade.html')

def signup(request):
	if request.method =='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{
		'form':form
		})
