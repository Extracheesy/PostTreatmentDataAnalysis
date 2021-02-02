from PyPDF2 import PdfFileReader, PdfFileWriter

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import os
import glob
import sys
import datetime
import pathlib
from os import path
from glob import glob

from PyPDF2 import PdfFileMerger


def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

def move_pdfs(output) :

    os.chdir(output)
    print(os.getcwd())
    print("tata +++++++++++++++++")

    os.chdir("..")
    print(os.getcwd())
    print("titi +++++++++++++++++")

    pdf_files = find_ext(".","pdf")

    for i in pdf_files :
        print("pdf file:     ",i)
        rename = output + "/" + i
        os.rename(i, rename)




def merge_pdfs(output) :

    os.chdir(output)

    pdf_files = find_ext(".", "pdf")

    merger = PdfFileMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()



