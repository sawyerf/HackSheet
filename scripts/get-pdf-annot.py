'''
    This program takes a PDF file and extracts anotations file from it.
'''
import fitz
import argparse as ap
from argparse import RawTextHelpFormatter
import requests
import io
    
def printAnotFile(doc):
    '''
        This function takes a PDF document (instance of fitz.Document)
            and print all annotations file for each page.
    '''
    for page in doc:
        for annot in page.annots():
            print(annot.get_file().decode())

if __name__ == "__main__":
    parser = ap.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-f", "--file", required=True, type=str, help='Path of your pdf file or http request')
    args = parser.parse_args()
    file = args.file
    
    if file.startswith('http://'):
        https_options = {'verify': False} if file.startswith('https') else {}
        r = requests.get(file, **https_options)
        content_pdf = r.content
        pdf_content = io.BytesIO(requests.get(file).content)
        doc = fitz.open(stream=pdf_content, filetype="pdf")
    else:
        doc = fitz.open(file)
    printAnotFile(doc)