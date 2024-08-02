import base64
import os
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QTextEdit
from docx import Document
from docx.shared import Pt, RGBColor


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
