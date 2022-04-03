import requests
from bs4 import BeautifulSoup
import pandas

mb_url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Multistorey" \
         "-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=North-area-Bangalore"
req = requests.get(mb_url)
content = req.content

soup = BeautifulSoup(content, "html.parser")

all_flat = soup. find_all("div", {"class": "mb-srp__card"})
scrapped_info_list = []

for flat in all_flat:
    flat_dic = {}
    flat_dic["type"] = flat.find("h2", {"class": "mb-srp__card--title"}).text
    try:
        flat_dic["name"] = flat.find("a", {"class": "mb-srp__card__society--name"}).text
    except AttributeError:
        flat_dic["name"] = None

    scrapped_info_list.append(flat_dic)

dataFrame = pandas.DataFrame(scrapped_info_list)
print("Creating CSV File.....")
dataFrame.to_csv("M_B.csv")
