import requests 
from bs4 import BeautifulSoup
from time import strptime
import os
import urllib


def change_month_to_number(word):
    if(len(word)<=2):
        return int(word)
    new = word[0].upper() + word[1:3].lower()
    return strptime(new,'%b').tm_mon

# This opens a handle to your file, in 'r' read mode
file_handle = open('input.txt', 'r')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
start_month,start_year=lines_list[0].split()
end_month,end_year=lines_list[1].split()
authors=[]
for author in (lines_list[2].split()):
    authors.append(author)
start_month=change_month_to_number(start_month)
end_month=change_month_to_number(end_month)
start_year=int(start_year)
end_year=int(end_year)
print("Starts from: ",start_month,start_year)
print("End at : ",end_month,end_year)

for year in range(start_year,end_year+1):
    if(year==start_year & year==end_year):
        for month in range(start_month,end_month+1):
            for author in authors:
                URL = "https://explosm.net/comics/archive/"+str(year)+"/"+str(month)+"/"+author.lower()
                r = requests.get(URL) 
                soup = BeautifulSoup(r.content, 'html5lib') 
                table = soup.findAll('div', attrs = {'class':'row collapse'})
                for div in table:
                    URL1="https://explosm.net"+div.a['href']
                    date=div.find('div',attrs= { 'id':'comic-author'}).text.split()[0]
                    print(date)
                    r1 = requests.get(URL1)
                    soup1 = BeautifulSoup(r1.content, 'html5lib')
                    img=soup1.findAll("img", {"id":"main-comic"})[0]['src']
                    print(img)
                    if not os.path.exists(str(year)+"/"+str(month)):
                        os.makedirs(str(year)+"/"+str(month))
                    urllib.request.urlretrieve("https:"+img,str(year)+"/"+str(month)+"/"+date+"-"+author.lower()+".png")
                    
                    
    elif(year==start_year):
        for month in range(start_month,13):
            for author in authors:
                URL = "https://explosm.net/comics/archive/"+str(year)+"/"+str(month)+"/"+author.lower()
                r = requests.get(URL) 
                soup = BeautifulSoup(r.content, 'html5lib') 
                table = soup.findAll('div', attrs = {'class':'row collapse'})
                for div in table:
                    URL1="https://explosm.net"+div.a['href']
                    date=div.find('div',attrs= { 'id':'comic-author'}).text.split()[0]
                    print(date)
                    r1 = requests.get(URL1)
                    soup1 = BeautifulSoup(r1.content, 'html5lib')
                    img=soup1.findAll("img", {"id":"main-comic"})[0]['src']
                    print(img)
                    if not os.path.exists(str(year)+"/"+str(month)):
                        os.makedirs(str(year)+"/"+str(month))
                    urllib.request.urlretrieve("https:"+img,str(year)+"/"+str(month)+"/"+date+"-"+author.lower()+".png")
              
    elif(year==end_year):
        for month in range(1,end_month+1):
            for author in authors:
                URL = "https://explosm.net/comics/archive/"+str(year)+"/"+str(month)+"/"+author.lower()
                r = requests.get(URL) 
                soup = BeautifulSoup(r.content, 'html5lib') 
                table = soup.findAll('div', attrs = {'class':'row collapse'})
                for div in table:
                    URL1="https://explosm.net"+div.a['href']
                    date=div.find('div',attrs= { 'id':'comic-author'}).text.split()[0]
                    print(date)
                    r1 = requests.get(URL1)
                    soup1 = BeautifulSoup(r1.content, 'html5lib')
                    img=soup1.findAll("img", {"id":"main-comic"})[0]['src']
                    print(img)
                    if not os.path.exists(str(year)+"/"+str(month)):
                        os.makedirs(str(year)+"/"+str(month))
                    urllib.request.urlretrieve("https:"+img,str(year)+"/"+str(month)+"/"+date+"-"+author.lower()+".png")
               
    else:
        for month in range(1,13):
            for author in authors:
                URL = "https://explosm.net/comics/archive/"+str(year)+"/"+str(month)+"/"+author.lower()
                r = requests.get(URL) 
                soup = BeautifulSoup(r.content, 'html5lib') 
                table = soup.findAll('div', attrs = {'class':'row collapse'})
                for div in table:
                    URL1="https://explosm.net"+div.a['href']
                    date=div.find('div',attrs= { 'id':'comic-author'}).text.split()[0]
                    print(date)
                    r1 = requests.get(URL1)
                    soup1 = BeautifulSoup(r1.content, 'html5lib')
                    img=soup1.findAll("img", {"id":"main-comic"})[0]['src']
                    print(img)
                    if not os.path.exists(str(year)+"/"+str(month)):
                        os.makedirs(str(year)+"/"+str(month))
                    urllib.request.urlretrieve("https:"+img,str(year)+"/"+str(month)+"/"+date+"-"+author.lower()+".png")
               
print("******   All files downloaded. Enjoy the Comics    *******")