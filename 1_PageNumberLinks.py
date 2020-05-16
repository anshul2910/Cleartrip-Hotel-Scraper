import random
import requests
import time
import lxml
import re
from selenium import webdriver
from bs4 import BeautifulSoup


# browser = webdriver.Chrome("C:\\Users\\Anshul\\Desktop\\Instagram\\chromedriver_win32\\chromedriver.exe")
# browser = webdriver.Edge("C:\\Users\\Anshul\\Desktop\\Instagram\\edgedriver_win64\\msedgedriver.exe")

baseURL = "https://me.cleartrip.com/"
cityURL = "https://me.cleartrip.com/hotels/united-states/miami"  #change cityURL for fetching pageNumberLinks of different city.

# browser.get(cityUrl)

page = requests.get(cityURL)
soup = BeautifulSoup(page.text, 'html.parser')

# Determing total number of pages for a particular city 
# (currently, determing for Miami)

pageNumber = soup.select('.pagination a')
pageNumber = pageNumber[:-1]
print("Total Number of Pages :", len(pageNumber) + 1)


# Links of all pageNumbers(40) in this case:
for i in pageNumber:
    pageNumberLinks = []
    pageNumberLinks = (baseURL + i.get('href'))
    with open("PageNumberLinks.txt", 'a') as file:
        file.write(pageNumberLinks + "\n")
        

