# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:00:08 2020

@author: wsx5
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 03:50:34 2020

@author: Ben
"""
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup   

#gets the percentages of each religion and puts them in a list
def webscrapingpercentages(url):
    URL = 'https://en.wikipedia.org/wiki/Religion_in_' + url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
    results = soup.find(class_ = 'PieChartTemplate thumb tright')
    if results is None:
       print("restart, you spelled it wrong or put a country that doesn\'t have data on wikipedia, Japan codes it differently so I can't scrape it")
       raise SystemExit
    else:
        percentages = results.find_all('div', class_="legend")
        plist = []
        for percentage in percentages:
            percentagetext = percentage.get_text().strip().split()
            plist.append(percentagetext[-1])
        return plist

#gets the labels of each religion and puts them in a list
def webscrapinglabels(url):
    URL = 'https://en.wikipedia.org/wiki/Religion_in_' + url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
    results = soup.find(class_ = 'PieChartTemplate thumb tright')
    if results is None:
       print("restart, you spelled it wrong or put a country that doesn\'t have data on wikipedia, Japan codes it differently so I can't scrape it")
       raise SystemExit
    else:
        weblabeless = results.find_all('div', class_="legend")
        weblabels = []
        for weblis in weblabeless:
            weblist = weblis.get_text().strip().split()
            del weblist[-1]
            weblabels.append(weblist)
        return weblabels

inputst = input('Put Country Name Here (put _ underscores instead of spaces, Japan doesn\'t work): \n')
#just put a religion_in wikipedia url
if inputst  == "Ireland":
    inputst  = 'the_Republic_of_Ireland'
if inputst == "America" or inputst == "america" or inputst == "usa":
    inputst = "United_States"

temperc = webscrapingpercentages(inputst)
templabel = webscrapinglabels(inputst )

        

#takes the list from webscrapinglabels formats each set of words from each div tag into their own list
k = ""
for i in range(len(templabel)):
  if len(templabel[i]) > 1:
    k = " ".join(templabel[i])
    temp_lis = []
    temp_lis.append(k)
    templabel[i] = temp_lis


#puts the formatted webscrapinglabels list into the labels list
labels = []
for label in templabel:
    labels.extend(label)
    
#puts the percentages from webscrapingpercentages in the sizes list
sizes = []
for percentages in temperc:
    sizes.append(float(percentages[1:-2]))
    
#sets a list of 10 colors for each potential religion
colors_1 = ['#52489C', '#7EB77F', '#A491D3', '#F57A7A','#FFCAB1','rosybrown','lightgoldenrodyellow','navajowhite','darkgray','mediumaquamarine','white','red']

#sets the colors sequentially that are necessary for the given piechart
colors = [] 
for color in range(len(sizes)):
    colors.append(colors_1[color])
   
#explodes the largest percentage by 0.1
explode = [0.1]  
for explod in range(len(sizes)-1):
    explode.append(0.0)

#plots the piehchart and saves it as a png
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=sizes, autopct='%1.1f%%',
        shadow=True, startangle=360, labeldistance = 1.2, colors=colors, explode=explode)
plt.legend(labels,)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
plt.savefig('saved_figure.png')
    



