# -*- coding: utf-8 -*-
"""

https://techacademy.jp/magazine/22374

"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

user_name = os.environ['USERPROFILE'].replace('\\', '/')

input_path = user_name + '/Desktop/text.pdf'
output_path = user_name + '/Desktop/text_from_pdf.txt'

manager = PDFResourceManager()

with open(output_path, "wb") as output:
    with open(input_path, 'rb') as input:
        with TextConverter(manager, output, codec='utf-8', laparams=LAParams()) as conv:
            interpreter = PDFPageInterpreter(manager, conv)
            for page in PDFPage.get_pages(input):
                interpreter.process_page(page)