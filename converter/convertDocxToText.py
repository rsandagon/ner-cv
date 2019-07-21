from docx import Document


def convert_docx_to_text(path):
	document = Document(path)
	return "\n".join([para.text for para in document.paragraphs])
