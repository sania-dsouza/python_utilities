import requests
from bs4 import BeautifulSoup as bs

def getNumberDays(monNo, year):
    if monNo in [1,3,5,7,8,10,12]:
        return 31
    elif monNo in [4,6,9,11]:
        return 30
    else:
        if year%4 : 
            return 28
        else:
            return 29

def getYearlyRawData(webLink, year):

    # initialize final variable which which
    # will hold the year's headlines (all months)
    yearlyData, dayHeadlines, monthHeadlines = [], [], []
    for month in range(1,13):
        webLink2 = webLink + str(month) + "/"

        days = getNumberDays(month, year)    # get the number of days in the selected month

        for day in range(1, days+1):          # get the headlines of each day
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