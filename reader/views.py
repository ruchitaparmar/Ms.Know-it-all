from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .pdfToJrg import getResultTuple
from .searchEngine import getMeaning, stripQuery
# Create your views here.


def upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		fs.save('reader/pdfDoc/' + myfile.name, myfile)
		textString, jargon = getResultTuple(myfile.name)
		readerDict = {}
		readerDict['text'] = textString
		readerDict['jargon'] = jargon
		readerDict['meaning'] = [getMeaning(stripQuery(i), i) for i in jargon]
		return render(request, 'reader.html', readerDict)
	else:
		return render(request, 'upload.html')
