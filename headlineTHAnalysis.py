# Headline Analysis of leading Indian newspaper The Hindu
# this program analyzes the headlines of the newspaper for a location 
# over a span of 20 years starting 2000 till 2019 

import requests
from bs4 import BeautifulSoup as bs
from ttictoc import TicToc
import re, nltk
#from nltk.stem import PorterStemmer 
#nltk.download('stopwords')     # needs to be done once

from helperFunctions import dataCollectorFunctions as dc

# get the data
# source : The Hindu, for example, the format of the page link: https://www.thehindu.com/archive/web/2009/08/18/
startYear = 2010
lastYear = 2010
#ps = PorterStemmer()
for year in range(startYear, lastYear+1):

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
    tokenWords = re.findall("\w+", str(data2transform))
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
    print(words_final)
    # evaluate the data

    # 
