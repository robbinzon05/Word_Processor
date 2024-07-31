from PyQt5.QtGui import QTextCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from docx import Document
from docx.shared import Pt
from PyQt5.QtWidgets import QTextEdit


def open_txt(file_path, text_edit: QTextEdit):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        text_edit.setText(data)


def open_docx(file_path, text_edit: QTextEdit):
    doc = Document(file_path)
    html_content = []
    for para in doc.paragraphs:
        paragraph_html = "<p>"
        for run in para.runs:
            run_html = run.text
            if run.bold:
                run_html = f"<b>{run_html}</b>"
            if run.italic:
                run_html = f"<i>{run_html}</i>"
            if run.underline:
                run_html = f"<u>{run_html}</u>"
            if run.font.size:
                run_html = f'<span style="font-size: {run.font.size.pt}pt;">{run_html}</span>'
            paragraph_html += run_html
        paragraph_html += "</p>"
        html_content.append(paragraph_html)
    text_edit.setHtml(''.join(html_content))


def save_txt(file_path, text_edit: QTextEdit):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text_edit.toPlainText())


def save_docx(file_path, text_edit: QTextEdit):
    doc = Document()
    cursor = QTextCursor(text_edit.document())

    def apply_char_format(run, char_format):
        if char_format.fontItalic():
            run.italic = True
        if char_format.fontWeight() == 75:
            run.bold = True
        if char_format.fontUnderline():
            run.underline = True
        if char_format.fontPointSize() > 0:
            run.font.size = Pt(char_format.fontPointSize())

    block = cursor.block()

    while block.isValid():
        paragraph = doc.add_paragraph()
        iter = block.begin()
        while iter != block.end():
            fragment = iter.fragment()
            if fragment.isValid():
                run = paragraph.add_run(fragment.text())
                apply_char_format(run, fragment.charFormat())
            iter += 1
        block = block.next()

    doc.save(file_path)


def save_pdf(file_path, text_edit: QTextEdit):
    html_content = text_edit.toHtml()
    web_view = QWebEngineView()
    web_view.setHtml(html_content)

    def convert_to_pdf():
        web_view.page().printToPdf(file_path)

    web_view.loadFinished.connect(convert_to_pdf)
