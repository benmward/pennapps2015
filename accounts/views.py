from django.shortcuts import render

# Create your views here.

def Login(request):
	return render(request,'login.html')

def Logout(request):
	return render(request, 'index.html')
