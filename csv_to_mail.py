#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_sender=""
password=""
subject="subscription activated"

with open("emails.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        text="hello"+line[1]+"your"+line[2]+"has been activated"
        print(text)
        email_send=line[0]
        msg=MIMEMultipart()
        msg["from"]=email_user
        msg["to"]=email_send
        msg["subject"]=subject
        msg.attach(MIMEText(text,"plain"))
        text=msg.as_string()
        
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login=(email_user,email_password)
        server.sendmail=(email_user,email_send,text)
        
        server.quit()
        


# In[ ]:




