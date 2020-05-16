import random
import requests
import time
import lxml
import os
import data
from selenium import webdriver
from bs4 import BeautifulSoup



# browser = webdriver.Chrome("C:\\Users\\Anshul\\Desktop\\Instagram\\chromedriver_win32\\chromedriver.exe")
# browser = webdriver.Edge("C:\\Users\\Anshul\\Desktop\\Instagram\\edgedriver_win64\\msedgedriver.exe")


baseURL = data.baseURL
cityURL = data.cityURL

cityURLS = []
with open ("PageNumberLinks.txt", 'r') as file:
    l = file.readlines()
    cityURLS = []
    cityURLS.append(cityURL)
    for i in l:
        cityURLS.append(i.strip())
    
print(cityURLS)

res = requests.get(cityURL)
soup = BeautifulSoup(res.text, 'lxml')

for apple in cityURLS:
    #browser.get(apple)
    res = requests.get(apple)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    hotelRaw = soup.select('#hotelsList a')
    for i in hotelRaw:
        if i != None:
            hotelsURL = (baseURL + str(i.get('href')))
            # print(hotelsURL)
            with open ("HotelNotCleaned.txt", 'a') as file:
                file.write(hotelsURL + "\n")

with open("HotelNotCleaned.txt", 'r') as file:
    lines = file.readlines()
with open("HotelLinks.txt", "a") as file:
    for line in lines:
        if (len(line) > 30):
            file.write(line)

os.remove("HotelNotCleaned.txt") #file removed after cleaning as it contains the raw data 


