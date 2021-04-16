from PyPDF2 import PdfFileReader


def extrair_texto(pdf_path):
	with open(pdf_path, 'rb') as f:
		pdf = PdfFileReader(f)
		number_of_pages = pdf.getNumPages()
		mensagem = ''
		for page in range(number_of_pages):
			pg = pdf.getPage(page)
			texto = pg.extractText()
			mensagem += ''.join(texto)
		return mensagem


if __name__ == '__main__':
	print(extrair_texto('data/portoeditora_gilvicente_barcainferno.pdf'))
