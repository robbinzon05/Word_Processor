import base64
import os
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTextEdit
from docx import Document
from docx.shared import Pt


def open_txt(file_path, text_edit: QTextEdit):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        text_edit.setText(data)


def open_docx(file_path, text_edit: QTextEdit):
    temp_dir = os.path.join(os.path.dirname(file_path), "temp_images")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    doc = Document(file_path)
    html_content = ""

    for para in doc.paragraphs:
        for run in para.runs:
            if run.text:
                html_content += run.text.replace('\n', '<br>') + ' '
            for inline_shape in run.element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing'):
                for blip in inline_shape.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
                    rID = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    image_part = doc.part.related_parts[rID]
                    image_data = image_part.blob
                    encoded_image = base64.b64encode(image_data).decode("utf-8")
                    img_tag = f'<img src="data:image/png;base64,{encoded_image}"/>'
                    html_content += img_tag + ' '
        html_content += '<br>'

    text_edit.setHtml(html_content)


def save_txt(file_path, text_edit: QTextEdit):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text_edit.toPlainText())


def add_image(paragraph, image_path):
    run = paragraph.add_run()
    run.add_picture(image_path)


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
                if fragment.charFormat().isImageFormat():
                    image_format = fragment.charFormat().toImageFormat()
                    image_path = image_format.name()
                    add_image(paragraph, image_path)
                else:
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
