from django.shortcuts import render
from reader.searchEngine import stripQuery, getMeaning, getCourses
# Create your views here.


def homepage(request):
	return render(request, 'homepage.html')


def cs(request):
	return render(request, 'computer-science.html')


def business(request):
	return render(request, 'business.html')


def astronomy(request):
	return render(request, 'astronomy.html')


def search(request, domain, showDomain=False):
	if request.method == 'POST':
		search_query = str(request.POST.get('srch'))

		query = stripQuery(search_query)
		meaning = getMeaning(query, search_query)
		courses = getCourses(query, domain=domain, showDomain=showDomain)
		results = {}
		results['meaning'] = meaning
		results['courses'] = courses
		return render(request, 'searchResult.html', results)
	else:
		return render(request, domain + '.html')


def searchCs(request):
	return search(request, 'computer-science', True)


def searchBusiness(request):
	return search(request, 'business', True)


def searchAstronomy(request):
	return search(request, 'astronomy')


def searchHome(request):
	return search(request, 'homepage')
