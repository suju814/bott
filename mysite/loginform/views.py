from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def homes(request):
	
	return render(request,'homes.html')




def index(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, "index.html", data)


def get_crypto_data():
	url = 'https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_ETH'
	parameters ={
		'id':'10'
	}
	headers = {
	  'Accepts': 'application/json',
	  'X-CMC_PRO_API_KEY': 'PE7QD910-N2TDEPAP-LZILGG72-E3ICHKJW',
	}

	session = Session()
	session.headers.update(headers)

	try:
	  response = session.get(url, params=parameters)
	  data = json.loads(response.text)
	  return data
	except (ConnectionError, Timeout, TooManyRedirects) as e:
	  print(e)

def main(request):

	
	return render(request,'main.html')

def home(request):
	
	return render(request,'home.html')


def logo(request):
	
	return render(request,'logo.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
"""
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
"""
