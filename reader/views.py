from django.shortcuts import render
# Create your views here.


def reader(request):
	return render(request, 'reader.html')
