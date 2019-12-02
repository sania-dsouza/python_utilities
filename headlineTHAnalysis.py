# Headline Analysis of leading Indian newspaper The Hindu
# this program analyzes the headlines of the newspaper for a location 
# over a span of 20 years starting 2000 till 2019 

import requests
from bs4 import BeautifulSoup as bs
from ttictoc import TicToc
import re, nltk
import matplotlib.pyplot as plt
import seaborn as sns
#from nltk.stem import PorterStemmer 
#nltk.download('stopwords')     # needs to be done once
from helperFunctions import dataCollectorFunctions as dc
from collections import Counter

# initialise a dictionary that will hold the yearly data as elements
final_YearlyData = {}

# get the data
# source : The Hindu, for example, the format of the page link: https://www.thehindu.com/archive/web/2009/08/18/
startYear = 2010
lastYear = 2019

#ps = PorterStemmer()
for year in range(startYear, lastYear+1):

    words_final = []   #reinitialize the yearly data list 
    # get the data to analyze
    t = TicToc()
    t.tic()
    webLink = "https://www.thehindu.com/archive/web/"+str(year)+"/"
    data2transform = dc.getYearlyRawData(webLink,year)
    #print(data2transform)    #returns a list of headlines from the year range above for all months and all days
    t.toc()
    print("Time elapsed:", t.elapsed, "s")

    # transform the data
    # Input: list with headlines 
    # tasks involved: 
    # tokenize the words
    tokenWords = re.findall("[A-Za-z]+", str(data2transform))
    words, words_final = [], []
    for w in tokenWords:
        words.append(w.lower())
    
    # remove stop words
    # generate stop words
    sw = nltk.corpus.stopwords.words('english')
    
    # remove stop words from list of words
    for word in words:
        if word not in sw:
            words_final.append(word)
    
    final_YearlyData[year] = words_final

# evaluate the data
# get the most frequently-used words and plot the word vs count graph
# get the values of the dictionary final_YearlyData as separate values in this list

dict_Values = [final_YearlyData[i] for i in final_YearlyData.keys()]
# print(dict_Values)
xs, ys = [], []
for i in dict_Values:
    mostFreq = Counter(i).most_common(1)
    xs.append(mostFreq[0][0])
    ys.append(mostFreq[0][1])
    
# plot the year vs the counter of the most-used word (probably a function to calculate this)

plt.plot(xs, ys)
yr = 0
for x,y in zip(xs, ys):
    label = str(startYear + yr)
    plt.annotate(label, (x,y), textcoords = "offset points", xytext = (0,10), ha = 'center')
    yr = yr + 1
plt.show()



# This is not the required solution here
# for i in range(0,(lastYear-startYear)):
#     freqdist2 = nltk.FreqDist(dict_Values[i])
#     freqdist1.append(freqdist2[1])  # get the top-most important word in a year's headlines and compare with the rest of the years

# freqdist1.plot()