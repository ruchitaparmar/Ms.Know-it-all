from django.shortcuts import render
# Create your views here.


def homepage(request):
	return render(request, 'homepage.html')


def cs(request):
	return render(request, 'computer-science.html')


def business(request):
	return render(request, 'business.html')


def astronomy(request):
	return render(request, 'astronomy.html')
