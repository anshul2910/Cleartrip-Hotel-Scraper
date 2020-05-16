import re
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
import json

def download_hotel_data(hotel_url):
    url_client = urlopen(hotel_url)
    page_html = url_client.read()
    page_soup=soup(page_html,'html.parser')
    url_client.close()
    return page_soup
def find_name(page_soup):
    try: 
        hotel_name=page_soup.title
        hotel_name=hotel_name.text
        hotel_name = hotel_name.split(',')[0]
       
        return hotel_name
    except:
        return None
def hotel_address(page_soup):
    try:
        hotel_address = page_soup.title
        hotel_address = hotel_address.text
        hotel_address = hotel_address.split(',')[1]
        return hotel_address
    except:
        return None
def hotel_price(page_soup):
    try:
        hotel_price=page_soup.find('p',{'class':'minprice'}).contents[-1]
        return hotel_price
    except:
        return None
def hotel_rating(page_soup):
    try:
        rating=page_soup.find(class_="inline row trustBadges")
        hotel_tarating=rating.find('small').text
        return hotel_tarating
    except:
        return None
def hotel_dscr(page_soup):
    data=""
    try:
        abouthotel=page_soup.find('div', class_='amenitiesCategory')
        about=abouthotel.find_all('p')
        for p in about:
            data = data + p.text
        return data
    except:
        return None
def hotel_others(page_soup):
    dct={}
    others=page_soup.find_all('div',{'class':'amenities-category'})
    tstst = [i for i in others]
    try:
        check_in=tstst[0].text.split(" ")[5]# if tstst[0].text.split(" ")[5] else 0
        check_out=tstst[0].text.split(" ")[9]
        rooms_no=tstst[0].text.split(" ")[13]# if tstst[0].text.split(" ")[13] else 0
        dct['check_in']=check_in
        dct['check_out']=check_out
        dct['rooms']=rooms_no
        others=tstst[1]
        heads=[i.text for i in others.find_all('div')]
        lsts=others.findAll('ul',{'class':'list-inline amenities'})
        lk=0
        for i in lsts:
            key=heads[lk].lower()
            key=re.sub('[^ a-zA-Z0-9]','',key)
            key='_'.join(key.split(' '))
            dct[key]=i.text.split("  ")[1:]
            lk+=1
        return dct
    except:
        return None
def create_dict(url):
    page_soup=download_hotel_data(url)
    dct=dict()
    dct['hotel_name']=find_name(page_soup)
    dct['hotel_url']=str(url)
    dct['hotel_address']=hotel_address(page_soup)
    dct['hotel_rating']=hotel_rating(page_soup)
    dct['hotel_price']=hotel_price(page_soup)
    dct['hotel_info']=hotel_dscr(page_soup)
    others=hotel_others(page_soup)
    try:
        for key in others:
            dct[key]=others[key]
        return dct
    except:
        return dct


# download_hotel_data("https://me.cleartrip.com//hotels/details/king-grove-tides-south-beach-367317?c=180520|190520&r=2,0&shwb=true&compId=&fr=1&ur=1&urt=featured&stp=chmm&pahCCRequired=true&op=true&area=&sd=1553075158552&lowRate=true&dest_code=&tags=#")
# print(find_name())

with open ("HotelLinks.txt", 'r') as file:
    l = file.readlines()
    allHotels = []
    for i in l:
        allHotels.append(i.strip())

ls_test = []
for url in allHotels:
    # print(url)
    ls_test.append(create_dict(url))
# print(ls_test)

with open('slice_data.json', 'w') as fp: #dumping test dataset
    json.dump(ls_test, fp)