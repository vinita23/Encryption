#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PyPDF4
import tkinter
from PyPDF4 import PdfFileReader, PdfFileWriter
from tkinter import filedialog
root=tkinter.Tk()
root.withdraw()
file_name=filedialog.askopenfilename()
pdf_file=open(file_name,'rb')
input_pdf=PyPDF4.PdfFileReader(pdf_file)
pages_num=input_pdf.numPages
output=PyPDF4.PdfFileWriter()
for i in range(pages_num):
    input_pdf=PyPDF4.PdfFileReader(pdf_file)
    output.addPage(input_pdf.getPage(i))
    output.encrypt("PASS")
    with open("pass1.pdf","wb") as outputStream:
        output.write(outputStream)
pdf_file.close()        
        
    


# In[ ]:


from PyPDF4 import PdfFileReader, PdfFileWriter
from tkinter import filedialog
import os
root=tkinter.Tk()
root.withdraw()
#file_name=filedialog.askopenfilename()
folder=C:\Users\vinit\Downloads\MyDocuments
for i in os.walk(folder):
    print(i)
pdf_file=open(file_name,'rb')
input_pdf=PyPDF4.PdfFileReader(pdf_file)
pages_num=input_pdf.numPages
output=PyPDF4.PdfFileWriter()
for i in range(pages_num):
    input_pdf=PyPDF4.PdfFileReader(pdf_file)
    output.addPage(input_pdf.getPage(i))
    output.encrypt("PASS")
    with open("pass.pdf","wb") as outputStream:
        output.write(outputStream)
pdf_file.close()        


# In[ ]:


import PyPDF4
from datetime import datetime
from datetime import timedelta
root=tkinter.Tk()
root.withdraw()
file_name=filedialog.askopenfilename()
def file_encrypt_datetime():
        current_time = datetime.now()
        print(current_time)
        modified_time = current_time.replace(microsecond=0)
        print(modified_time)
        my_time_format = "%Y-%m-%d %H-%M-%S"
        converted_format_time = datetime.strftime(modified_time, my_time_format)
        return converted_format_time

    
def database(file_name, file_size, f_datetime, enpwd):
        connection = sqlite3.connect("PDF_data.db")
        c = connection.cursor()
        c.execute("""CREATE TABLE EncryptPDF("pdf_file_name" text,
        "pdf_size" integer, 
        "date_time" integer,
        "encrypted" text)""")
        c.execute(f'INSERT INTO EncryptedPDF(pdf_file_name, pdf_file_size, date_time_of_encryption, encrypted_pwd)'                    f"VALUES ('{file_name}', '{size}', '{datetime}', '{encrp}')")
        connection.commit()
        db_select = """SELECT * FROM EncryptPDF"""
        connection.execute(db_select)
        connection.close()    
    
def encrypt_pdf(input_pdf: str, password: str):
    input_pdf=PyPDF4.PdfFileReader(input_pdf)
    output=PyPDF4.PdfFileWriter()
    pages_num=input_pdf.numPages
    for i in range(pages_num):
        output.addPage(input_pdf.getPage(i))
    output.encrypt(password)
    with open("pr.pdf","wb") as outputStream:
        output.write(outputStream)
encrypt_pdf("Passport.pdf","Vinita")        
        


# In[ ]:





# In[ ]:




