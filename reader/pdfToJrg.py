import enchant
import nltk
import re

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine


def merge(words):
	str = ""
	for word in words:
		str += word + " "

	return str


def uniq(input):
	output = []
	for x in input:
		if x not in output:
			output.append(x)
	return output


def getResultTuple(myFile):
	with open(r'reader/pdfDoc/' + myFile, 'rb') as fp:
		parser = PDFParser(fp)
		doc = PDFDocument()
		parser.set_document(doc)
		doc.set_parser(parser)
		doc.initialize('')
		rsrcmgr = PDFResourceManager()
		laparams = LAParams()
		device = PDFPageAggregator(rsrcmgr, laparams=laparams)
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		return getText(doc, interpreter, device)


def getText(doc, interpreter, device):
	pages = []
	textDoc = ''
	for page in doc.get_pages():
		interpreter.process_page(page)
		layout = device.get_result()
		for lt_obj in layout:
			if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
				pages.append(lt_obj.get_text())
				textDoc += lt_obj.get_text()
	jargon = getJargon(pages)
	return (textDoc, jargon)


def getJargon(pages):
	jargons = []
	d = enchant.Dict("en_US")

	# Iterate over a list of string of pages
	tagged_sentence = nltk.tag.pos_tag(pages)
	edited_sentence = [word for word, tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']
	words = ' '.join(edited_sentence)
	words = re.sub("[^a-zA-Z]", " ", words).split()

	# words = nltk.word_tokenize(page)
	for word in words:
		if not d.check(word):
			jargons.append(word)

	jargons = uniq(jargons)
	return jargons


if __name__ == "__main__":
	getResultTuple('file.pdf')
