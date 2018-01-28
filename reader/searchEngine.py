import requests
from bs4 import BeautifulSoup


def fetchUrl(url):
	sourceHtml = requests.get(url).text
	return sourceHtml


def getCourses(query, domain, showDomain=False):
	if showDomain:
		url = "https://www.coursera.org/courses?_facet_changed_=true&domains="
		url += domain + "&languages=en&query=" + query
	else:
		url = "https://www.coursera.org/courses?&languages=en&query="
		url += query
	sourceHtml = fetchUrl(url)
	soup = BeautifulSoup(sourceHtml, 'lxml')
	try:
		soup = soup.find_all("a", {"class": "rc-OfferingCard"})
		result = ["https://www.coursera.org" + i["href"] for i in soup]
	except AttributeError:
		result = None
	return result


def getMeaning(query, queryInput):
	url = 'https://www.google.co.in/search?&q='
	url += query + '+meaning'
	sourceHtml = fetchUrl(url)
	soup = BeautifulSoup(sourceHtml, 'lxml')
	try:
		result = soup.find("div", {"class": "_sPg"}).text
	except AttributeError:
		try:
			soup = soup.find("table", {"style": "font-size:14px;width:100%"})
			soup = soup.find("li")
			result = queryInput + " : " + soup.text
		except AttributeError:
			result = False
	return result


def stripQuery(query):
	query = query.strip().replace(' ', '+')
	return query


if __name__ == "__main__":
	queryInput = input("Enter search query: ")
	domain = ["computer-science", "business"]
	domain = domain[1]
	query = stripQuery(queryInput)
	print("\nMeaning: " + getMeaning(query, queryInput))
	print("\n\nCourses:")
	print(getCourses(query, domain))
