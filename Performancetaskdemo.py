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

#gets the percentages of each religion and puts them in a list
from bs4 import BeautifulSoup
from shapely import wkt
import os
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import requests



def webscrapingpercentages(url):
    URL = 'https://en.wikipedia.org/wiki/Religion_in_' + url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
    results = soup.find(class_='PieChartTemplate thumb tright')
    if results is None:
       print("restart, you spelled it wrong or put a country that doesn\'t have data on wikipedia")
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
    results = soup.find(class_='PieChartTemplate thumb tright')
    if results is None:
       print("restart, you spelled it wrong or put a country that doesn\'t have data on wikipedia")
       raise SystemExit
    else:
        weblabeless = results.find_all('div', class_="legend")
        weblabels = []
        for weblis in weblabeless:
            weblist = weblis.get_text().strip().split()
            del weblist[-1]
            weblabels.append(weblist)
        return weblabels


inputst = input(
    'Put Country Name Here (put _ underscores instead of spaces): \n')
#just put a religion_in wikipedia url
if inputst == "Ireland":
    inputst = 'the_Republic_of_Ireland'
if inputst == "America" or inputst == "america" or inputst == "usa":
    inputst = "United_States"

temperc = webscrapingpercentages(inputst)
templabel = webscrapinglabels(inputst)


#takes the list from webscrapinglabels formats each set of words from each div tag into their own list
print(templabel)
k = ""
for i in range(len(templabel)):
  if len(templabel[i]) > 1:
    k = " ".join(templabel[i])
    temp_lis = []
    temp_lis.append(k)
    templabel[i] = temp_lis
print(templabel)

#puts the formatted webscrapinglabels list into the labels list
labels = []
for label in templabel:
    labels.extend(label)

#puts the percentages from webscrapingpercentages in the sizes list
sizes = []
for percentages in temperc:
    sizes.append(float(percentages[1:-2]))

#sets a list of 10 colors for each potential religion
colors_1 = ['#52489C', '#7EB77F', '#A491D3', '#F57A7A', '#FFCAB1', 'rosybrown', 'lightgoldenrodyellow',
            'navajowhite', 'darkgray', 'mediumaquamarine', 'ghostwhite', 'darkred', 'deepskyblue']

#sets the colors sequentially that are necessary for the given piechart

#explodes the largest percentage by 0.1
explode = [0.1]
for explod in range(len(sizes)-1):
    explode.append(0.0)

#plots the piehchart and saves it as a png
fig1, ax1 = plt.subplots()
ax1.pie(sizes, autopct='%1.2f%%',
        shadow=True, startangle=360, labeldistance=1.10, colors=colors_1, explode=explode, textprops={'fontsize': 6}, pctdistance=1.2)
plt.legend(labels)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
if inputst == "the_Republic_of_Ireland":
    inputst = 'Ireland'
if inputst == "United_States":
    inputst = 'United States of America'
empty_Frame = pd.DataFrame(columns=['Sizes', 'Labels', 'Country'])
print(empty_Frame)
if inputst == "United States of America":
    graphInput = input("Do you want to see a graph of The " + inputst + "'s religiosity? ")
else:
    graphInput = input("Do you want to see a graph of " + inputst + "'s religiosity? ")


def geoMap(graphInput, inputst, labels, sizes, empty_Frame):
    if graphInput.upper() == "YES":
        #Makes the Sizes and Labels into a Panda Dataframe
        if inputst == "the_Republic_of_Ireland":
            inputst = 'Ireland'
        if inputst == "United_States":
            inputst = 'United States of America'
        data_Set_List = []
        temp_list2 = []
        for i in range(len(sizes)):
            temp_list2.append(sizes[i])
            temp_list2.append(labels[i])
            data_Set_List.extend([temp_list2])
            temp_list2 = []
        data_Set_Frame = pd.DataFrame(
            data_Set_List, columns=['Sizes', 'Labels'])
        print(data_Set_Frame)
        data_Set_Frame_Sort = data_Set_Frame.sort_values(by="Sizes", ascending=False, ignore_index=True)
        dt_sort = data_Set_Frame_Sort.values.tolist()
        sizes = [dt_sort[0][0]]
        labels = [dt_sort[0][1]]
        data_set = [[sizes[0],labels[0],inputst]]
        country_Frame = pd.DataFrame(
            data_set, columns=['Sizes', 'Labels', 'Country'])
        empty_Frame = empty_Frame.append(country_Frame, ignore_index=True)
        print(empty_Frame)
        world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
        combined_Data = world.merge(
            empty_Frame, how="left", left_on=['name'], right_on=['Country'])
        combined_Data.to_csv('Temp.csv', index=False)
        combined_Data_Temp = pd.read_csv("Temp.csv")
        combined_Data_Temp['geometry'] = combined_Data_Temp['geometry'].apply(wkt.loads)
        cdt = gpd.GeoDataFrame(combined_Data_Temp, crs='epsg:4326')
        cdt.plot("Sizes", figsize=(30, 15), missing_kwds={
            "color": "grey",
            "edgecolor": "black",
            "label": "Missing Values"}, legend=True, legend_kwds={
            "label": "Religious uniformity in the world", "orientation": "horizontal"})
        plt.title("Presence of " + labels[0] + " in " + inputst)
        plt.show()
        restart = input("Do you want to keep going? ")
        if restart.upper() == "YES":
            inputst = input(
                'Put Country Name Here (put _ underscores instead of spaces): \n')
        #just put a religion_in wikipedia url
            if inputst == "Ireland":
                inputst = 'the_Republic_of_Ireland'
            if inputst == "America" or inputst == "america" or inputst == "usa":
                inputst = "United_States"

            temperc = webscrapingpercentages(inputst)
            templabel = webscrapinglabels(inputst)


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
            colors_1 = ['#52489C', '#7EB77F', '#A491D3', '#F57A7A', '#FFCAB1', 'rosybrown', 'lightgoldenrodyellow',
                        'navajowhite', 'darkgray', 'mediumaquamarine', 'ghostwhite', 'darkred', 'deepskyblue']

#sets the colors sequentially that are necessary for the given piechart

#explodes the largest percentage by 0.1
            explode = [0.1]
            for explod in range(len(sizes)-1):
                explode.append(0.0)

#plots the piehchart and saves it as a png
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, autopct='%1.2f%%',
                    shadow=True, startangle=360, labeldistance=1.10, colors=colors_1, explode=explode, textprops={'fontsize': 6}, pctdistance=1.6)
            plt.legend(labels)
            # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.axis('equal')
            plt.tight_layout()
            plt.show()
            if inputst == "the_Republic_of_Ireland":
                inputst = 'Ireland'
            if inputst == "United_States":
                inputst = 'United States of America'
            check = input("Do you want to see a graph of " +
                          inputst + "'s religiosity? ")
            if check.upper() == "YES":
                geoMap(graphInput, inputst, labels, sizes, empty_Frame)
            else:
                if os.path.exists("Temp.csv"):
                    os.remove("Temp.csv")
                raise SystemExit
        else:
            if os.path.exists("Temp.csv"):
                os.remove("Temp.csv")
            raise SystemExit
    else:
        if os.path.exists("Temp.csv"):
            os.remove("Temp.csv")
        raise SystemExit


geoMap(graphInput, inputst, labels, sizes, empty_Frame)
