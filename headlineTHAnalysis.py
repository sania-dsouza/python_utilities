# Headline Analysis of leading Indian newspaper The Hindu
# this program analyzes the headlines of the newspaper for a location 
# over a span of 20 years starting 2000 till 2019 

import requests
from bs4 import BeautifulSoup as bs
from ttictoc import TicToc

from helperFunctions import dataCollectorFunctions as dc

# get the data
# source : The Hindu, for example, the format of the page link: https://www.thehindu.com/archive/web/2009/08/18/
startYear = 2010
lastYear = 2019

for year in range(startYear, lastYear+1):
    t = TicToc()
    t.tic()
    webLink = "https://www.thehindu.com/archive/web/"+str(year)+"/"
    data2transform = dc.getYearlyRawData(webLink,year)
    print(data2transform)    #returns a list of headlines from the year range above for all months and all days
    t.toc()
    print("Time elapsed:", t.elapsed, "s")

    # transform the data

    # clean the data

    # evaluate the data

    # 
