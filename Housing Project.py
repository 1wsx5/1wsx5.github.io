# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:42:34 2020

@author: wsx5
"""
from operator import contains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import requests
import random
from bs4 import BeautifulSoup 
import os
import re
    
url = input('Put a city: ')
url2 = input("Put the abbreviation of the State that city is in: ")
options = Options()
options.add_argument("--app=http://www.google.com")
#options.add_argument("--headless")
options.add_argument("disable-infobars")
driver = webdriver.Chrome(executable_path='C:\\Users\\wsx5\\Downloads\\chromedriver.exe', options=options)
# Maximize the screen
driver.maximize_window()
driver.implicitly_wait(20)
URL = 'https://www.trulia.com/' + url2 + "/" + url
driver.get(URL)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def PropPrice():
    namefind = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-price']")
    randomstocklist = []
    for stocknames in namefind:
        stockname = stocknames.text
        randomstocklist.append(stockname)
    return randomstocklist


def PropAddress():
    w = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-address']")
    weblabels = []
    for weblis in w:
        weblist = weblis.text.strip().split()
        weblabels.append(weblist)
    k=""
    for i in range(len(weblabels)):
      if len(weblabels[i]) > 1:
            k = " ".join(weblabels[i])
            temp_lis = []
            temp_lis.append(k)
            weblabels[i] = temp_lis
    return weblabels

def PropBeds():
    namefind = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-beds']")
    randomstocklist = []
    for stocknames in namefind:
        stockname = stocknames.text
        randomstocklist.append(stockname)
    return randomstocklist

def PropBaths():
    namefind = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-baths']")
    randomstocklist = []
    for stocknames in namefind:
        stockname = stocknames.text
        randomstocklist.append(stockname)
    return randomstocklist

def PropSqft():
    namefound = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-card-details']")
    list = []
    for stocknampar in namefound:
        stocknamos = stocknampar.text.strip().split()
        list.append(stocknamos)
    #print(randomstocklist)
    k=""
    x=-1
    for i in range(len(list)):
      if len(list[i]) > 1:
        k = " ".join(list[i])
        temp_lis = []   
        temp_lis.append(k)
        list[i] = temp_lis
    namefind = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-floorSpace']")
    randomstocklist = []
    for stocknames in namefind:
        x+=1
        #print(stockname)
        #print(len(PrpPrice))
        #print(stockname)
        #print(list[x][0])h
        if 'sqft' not in list[x][0]:
            randomstocklist.append(" ")
            randomstocklist.append(stocknames.text)
        else:
            print(stocknames.text)
            stockname = stocknames.text
            print(stockname)
            randomstocklist.append(stockname)
    #print(randomstocklist)
    return randomstocklist

def PropListing():
    namefind = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-card-listing-summary']")
    randomstocklist = []
    for stocknames in namefind:
        stockname = stocknames.text
        randomstocklist.append(stockname)
    return randomstocklist

def PropDeets():
    namefound = driver.find_elements(By.XPATH, "//div[@data-testid = 'property-card-details']")
    list = []
    for stocknampar in namefound:
        stocknamos = stocknampar.text.strip().split()
        list.append(stocknamos)
    #print(randomstocklist)
    k=""
    for i in range(len(list)):
      if len(list[i]) > 1:
        k = " ".join(list[i])
        temp_lis = []
        temp_lis.append(k)
        list[i] = temp_lis
    #print(randomstocklist)
    #for word in randomstocklist:
        #re.findall(r"[\w']+|[.,!?;]", word[i])
        #randomstocklist.pop(randomstocklist[i]) 	
        #randomstocklist.insert(word[i])
    #print(randomstocklist)
    #print(randomstocklist[0][0])
    """
    for word in randomstocklist:
        for word in randomstocklist:
            if r')?' in word[i][0]: 
                a = word[i][0].split("(?<=)) ")
                randomstocklist.pop(randomstocklist[i][0])
                randomstocklist.insert(a)
            if 'sqft' in word [i][0]:
                b = word[i][0].split("(?<=\s{6}) ")
                randomstocklist.pop(randomstocklist[i][0])
                randomstocklist.insert(b)
            else:
                c= word[i][0].split("(?<=\s{3}) ")
                randomstocklist.pop(randomstocklist[i][0])
                randomstocklist.insert(c)
    """
    return list
#next = driver.find_element(By.XPATH, '//*[@id="resultsColumn"]/nav/ul/li[8]/a')
def DataCollect():
    #while (True):
        PrpDeets = PropDeets()
    #print(PrpDeets)
        PrpPrice = PropPrice()
        PrpAdd = PropAddress()
        PrpBeds = PropBeds()
        Prpbaths = PropBaths()
        PrpSqft = PropSqft()
        PrpListing = PropListing()
        #print(len(PrpPrice))
        #print(len(PrpSqft))
        print(PrpPrice)
        print(PrpSqft)
        data_Set_List = []
        temp_list2 = []
        for i in range(len(PrpDeets)):
            temp_list2.append(PrpPrice[i])
            temp_list2.append(PrpAdd[i])
            temp_list2.append(PrpBeds[i])
            temp_list2.append(Prpbaths[i])
            temp_list2.append(PrpSqft[i])
            temp_list2.append(PrpListing[i])
            data_Set_List.extend([temp_list2])
            temp_list2 = []
        #next.click()
        driver.close()
        return data_Set_List  

data_Set_List = DataCollect()
data_Set_Frame = pd.DataFrame(
            data_Set_List, columns=['Price', 'Address', 'Beds', 'Baths', 'Sqft', 'Listing'])
data_Set_Frame_Sort = data_Set_Frame.sort_values(by="Price", ascending=False, ignore_index=True)
data_Set_Frame_Sort.to_csv("Temp.csv", index=False)
combined_Data_Temp = pd.read_csv("Temp.csv")
print(combined_Data_Temp)
save = input("Do you want to save your data? ")
if save.upper() == "YES" or save.upper() == "Y":
    name = input("what do you want to name your program? ")
    data_Set_Frame.to_csv(name.strip() + '.csv', index=False)
    combined_Data_Temp = pd.read_csv(name.strip() + ".csv")
    print(combined_Data_Temp)
    if os.path.exists("Temp.csv"):
        os.remove("Temp.csv")
    raise SystemExit
else:
    if os.path.exists("Temp.csv"):
        os.remove("Temp.csv")
    raise SystemExit   





"""

filteredrandomstocklist = list(filter(None, randomstocklist))


x = random.randint(1,41)

base = 0
for i in range(0, x):
    base = ((x-1) * 8) + 9

    
r = randomizedstocks()
k = ""
for i in range(len(r)):
  if len(r[i]) > 1:
    k = " ".join(r[i])
    temp_lis = []
    temp_lis.append(k)
    r[i] = temp_lis

stocks = []
for stock in r:
    stocks.extend(stock)
    
f = input("Do you want to see a random popular stock (y/n): ")

if x == 0 and f == "y":
    print(str(stocks[x]) + " has been selected, which currently is worth " + str(filteredrandomstocklist[1][0]) + " per share")
elif f == "y" and x != 0: 
    print(str(stocks[x]) + " has been selected, which currently is worth " + str(filteredrandomstocklist[base][0]) + " per share")
elif f == "n":
    print("suit yourself then")
else:
    print("you typed something wrong, try that again")
"""