#!/usr/bin/python3
print("Content-type:text/html \n\n")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.imdb.com/search/title/?release_date=2019&sort=num_votes,desc&page=1"
uREQ = urlopen(url)
pageC = uREQ.read()
uREQ.close()
soup = BeautifulSoup(pageC,"html.parser")

name = soup.find_all('div',{'class':'lister-item-content'})
# print (name[0].h3.a.text)
for link in name:
    print(link.h3.a.text) 

date = soup.find_all('span', {'class':'lister-item-year text-muted unbold'})
for link0 in date:
    print (link0.text)

votes = soup.find_all('p', {'class':'sort-num_votes-visible'})
for link2 in votes:
    print(link2.find_all('span',{'name':'nv'})[0].string)

rating = soup.find_all('div', {'class':'inline-block ratings-imdb-rating'})
for link3 in rating:
    print (link3.text)

PG = soup.find_all('span', {'class':'certificate'})
for link6 in PG:
    print (link6.text)

runtime = soup.find_all('span', {'class':'runtime'})
for link7 in runtime:
    print (link7.text)

genre = soup.find_all('span', {'class':'genre'})
for link8 in genre:
    print (link8.text)

file=open("project.csv","w")
file.write("MovieName"+","+"Date"+","+ "Votes"+","+ "Rating"+","+"PG"+","+ "Runtime"+","+"Genre"+"\n")
for link,link0,link2,link3,link6,link7,link8 in zip(name, date, votes, rating, PG, runtime, genre):
    h = link.h3.a.text.strip()
    h = h.replace(',','')
    z = link0.text.strip()
    a = link2.find_all('span',{'name':'nv'})[0].string.strip()
    a = a.replace(',','')
    b = link3.text.strip()
    e = link6.text.strip()
    f = link7.text.strip()
    g = link8.text.strip()
    g = g.replace(',','')
    print(h,z,a,b,e,f,g)
    file.write(h+","+z+","+a+","+b+","+e+","+f+","+g+"\n")
file.close()

