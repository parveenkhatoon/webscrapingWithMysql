
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json


url="https://en.wikipedia.org/wiki/Python_(programming_language)"
data= requests.get(url)
soup=BeautifulSoup(data.text, "html.parser")
# print(soup1)
list1=""
for name in soup.find_all("div",class_="mw-parser-output"):
    for name1 in name.find_all("p")[:4]:
        name2=name1.text
        list1=list1+name2
print(list1)
my_file = open("readme.txt","w+")
file_data = my_file.write(list1)
print(file_data)

name3=list1.split()
for j in range(1,20):
    list_2=[]
    for i in name3:
        if len(i)==16:
            continue
        elif len(i)==j:
            list_2.append(i)
    print(f"li st_{j} = {list_2}")
