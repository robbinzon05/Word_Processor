from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyQt5.QtWidgets import QTextEdit


def open_txt(file_path, text_edit: QTextEdit):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        text_edit.setText(data)


def open_docx(file_path, text_edit: QTextEdit):
    doc = Document(file_path)
    full_text = [para.text for para in doc.paragraphs]
    text_edit.setText('\n'.join(full_text))


def save_txt(file_path, text_edit: QTextEdit):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text_edit.toPlainText())


def save_docx(file_path, text_edit: QTextEdit):
    doc = Document()
    doc.add_paragraph(text_edit.toPlainText())
    doc.save(file_path)


def save_pdf(file_path, text_edit: QTextEdit):
    c = canvas.Canvas(file_path, pagesize=letter)
    text = text_edit.toPlainText()
    text_object = c.beginText(40, 750)
    for line in text.split('\n'):
        text_object.textLine(line)
    c.drawText(text_object)
    c.showPage()
    c.save()