#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Amazon tracker price for an specific product. Automatic email will be sent when the price reaches goal.


# In[ ]:


#import libraries.

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[17]:


#connect to Amazon webpage.

URL = "https://www.amazon.co.uk/CITIZEN-87601587-Citizen-Armbanduhr-BM7108-81L/dp/B07HC7T67C/?_encoding=UTF8&pd_rd_w=PZDFu&content-id=amzn1.sym.ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_p=ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_r=0H4HF5YRW7CXA8KW8C1W&pd_rd_wg=l78J4&pd_rd_r=1b719cf7-651a-4006-9672-a5b1271394ff&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id="productTitle").get_text()
price1 = soup2.find(id="corePriceDisplay_desktop_feature_div").get_text()
title = title.strip()
price = price1.strip() [1:7]

#print(title)
#print(price)

import datetime
today = datetime.date.today()

#print (today)


# In[41]:


#Create the CSV file and create the headers and first row.

#import csv

#header = ["Item","Price","Date"]
#data = [title,price,today]

#with open ("Amazon price tracker web scrapper.csv", "w", newline="", encoding="UTF8") as f:
    #writer = csv.writer(f)
    #writer.writerow(header)
    #writer.writerow(data)


# In[39]:


#Apend new data to the CSV file.

with open ("Amazon price tracker web scrapper.csv", "a+", newline="", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


def check_price():
    
    URL = "https://www.amazon.co.uk/CITIZEN-87601587-Citizen-Armbanduhr-BM7108-81L/dp/B07HC7T67C/?_encoding=UTF8&pd_rd_w=PZDFu&content-id=amzn1.sym.ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_p=ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_r=0H4HF5YRW7CXA8KW8C1W&pd_rd_wg=l78J4&pd_rd_r=1b719cf7-651a-4006-9672-a5b1271394ff&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    title = soup2.find(id="productTitle").get_text()
    price1 = soup2.find(id="corePriceDisplay_desktop_feature_div").get_text()
    title = title.strip()
    price = price1.strip() [1:7]

    import datetime
    today = datetime.date.today()
    
    import csv
    header = ["Item","Price","Date"]
    data = [title,price,today]

    with open ("Amazon price tracker web scrapper.csv", "a+", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while (True):
    check_price()
    time.sleep(10000)


# In[45]:


import pandas as pd

data = pd.read_csv(r"C:\Users\Sarah Geberowicz\Amazon price tracker web scrapper.csv")

print (data)


# In[ ]:


# Automatic email when price drops.

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('alsixtoabal@gmail.com','password')
    
    subject = "The price dropped below the requested value!!!"
    body = "Link to buy: https://www.amazon.co.uk/CITIZEN-87601587-Citizen-Armbanduhr-BM7108-81L/dp/B07HC7T67C/?_encoding=UTF8&pd_rd_w=PZDFu&content-id=amzn1.sym.ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_p=ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_r=0H4HF5YRW7CXA8KW8C1W&pd_rd_wg=l78J4&pd_rd_r=1b719cf7-651a-4006-9672-a5b1271394ff&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('alsixtoabal@gmail.com', msg)

