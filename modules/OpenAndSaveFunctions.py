import base64
import os
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTextEdit
from docx import Document
from docx.shared import Pt, RGBColor


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

    def add_styles(run):
        styles = ""
        if run.bold:
            styles += "font-weight:bold;"
        if run.italic:
            styles += "font-style:italic;"
        if run.underline:
            styles += "text-decoration:underline;"
        if run.font.size:
            styles += f"font-size:{run.font.size.pt}pt;"
        if run.font.color and run.font.color.rgb:
            red, green, blue = run.font.color.rgb
            styles += f"color:rgb({red},{green},{blue});"
        return styles

    for para in doc.paragraphs:
        for run in para.runs:
            if run.text:
                styles = add_styles(run)
                html_content += f'<span style="{styles}">{run.text.replace(" ", "&nbsp;")}</span> '
            for inline_shape in run.element.findall(
                    './/{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing'):
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


def save_docx(file_path, text_edit):
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
        if char_format.foreground().color().isValid():
            qt_color = char_format.foreground().color()
            red = qt_color.red()
            green = qt_color.green()
            blue = qt_color.blue()
            run.font.color.rgb = RGBColor(red, green, blue)

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

    def replace_images_with_base64(html):
        import re
        import os

        def base64_image(match):
            image_path = match.group(1)
            if image_path.startswith(('http:', 'https:')):
                return match.group(0)
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
                encoded_image = base64.b64encode(image_data).decode("utf-8")
                mime_type = get_mime_type(image_path)
                return f'src="data:{mime_type};base64,{encoded_image}"'

        def get_mime_type(image_path):
            ext = os.path.splitext(image_path)[1].lower()
            return {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.gif': 'image/gif'
            }.get(ext, 'application/octet-stream')

        return re.sub(r'src=["\']([^"\']+)["\']', base64_image, html)

    html_content = replace_images_with_base64(html_content)

    web_view = QWebEngineView()
    web_view.setHtml(html_content)

    def convert_to_pdf():
        web_view.page().printToPdf(file_path)

    web_view.loadFinished.connect(convert_to_pdf)
