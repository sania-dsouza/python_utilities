# Headline Analysis of leading Indian newspaper The Hindu
# this program analyzes the headlines of the newspaper for a location 
# over a span of 20 years starting 2000 till 2019 

import requests
from bs4 import BeautifulSoup as bs
from ttictoc import TicToc

def getNumberDays(monNo, year):
    if monNo in [1,3,5,7,8,10,12]:
        return 31
    elif monNo in [4,6,9,11]:
        return 30
    else:
        if year%4 : 
            return 29
        else:
            return 28

def getYearlyRawData(webLink, year):

    # initialize final variable which which
    # will hold the year's headlines (all months)
    yearlyData, dayHeadlines, monthHeadlines = [], [], []
    for month in range(1,13):
        webLink2 = webLink + str(month) + "/"

        days = getNumberDays(month, year)    # get the number of days in the selected month

        for day in range(1,days+1):          # get the headlines of each day
            webLink1 = webLink2 + str(day) + "/"

            # get the link content in html and parse
            r = requests.get(webLink1)
            soup = bs(r.content, 'html.parser')

            # get the headlines here using BS
            heading = soup.find('h2', id='national')
            for li in heading.parent.parent.parent.find_all('li'):
                a = li.find('a')
                monthHeadlines.append(a.get_text())

        yearlyData.append(monthHeadlines)
        
    return yearlyData[0][1:]

# get the data
# source : The Hindu, for example, the format of the page link: https://www.thehindu.com/archive/web/2009/08/18/
startYear = 2010
lastYear = 2019

for year in range(startYear, lastYear+1):
    t = TicToc()
    t.tic()
    webLink = "https://www.thehindu.com/archive/web/"+str(year)+"/"
    data2transform = getYearlyRawData(webLink,year)
    print(data2transform)    #returns a list of headlines from the year range above for all months and all days
    t.toc()
    print("Time elapsed:", t.elapsed, "s")

    # transform the data

    # clean the data

    # evaluate the data

    # 
