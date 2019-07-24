import docx2txt


def convert_docx_to_text(path):
	return docx2txt.process(path)
