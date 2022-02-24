import csv
from attr import attrs
import requests
from bs4 import BeautifulSoup
import math

url="http://www.alba.co.kr/"


def url_number(list): 
     inform_again = requests.get(list)

     inform_agian_soup = BeautifulSoup(inform_again.text, "lxml")
     page_number = inform_agian_soup.find(
        "p", {"class": "jobCount"}).find("strong")
     page_number = page_number.get_text()
     page_number = (page_number.replace(",", ""))
     page_number = math.ceil(int(page_number)/50)
     
     return page_number   
 #페이지 넘버를 얻어주는 함수 => 

def url_load(list,company):
    number=url_number(list)
    filename=company
    f = open(filename,"w",encoding="utf-8-sig", newline="")
    writer=csv.writer(f) 
    writer.writerow(['place','title','time','pay','date'])
    
    for i in range(1,number+1):
      URL=f"{list}/job/brand/?page={i}"
      print(URL)
      inform_again = requests.get(URL)

      inform_agian_soup = BeautifulSoup(inform_again.text, "lxml")   
      data_rows = inform_agian_soup.find("div",{"id":"NormalInfo"})#설명 뜯는거
      columns = data_rows.find_all("tr", attrs={"id": False, "class": True})


      for column in columns:
        local=column.find("td",{"class":"local first"}).get_text()
        company=column.find("span",attrs={"class":"company"}).get_text()
        date=column.find("td",{"class":"data"}).get_text()
        pay=column.find("td",{"class":"pay"}).get_text()
        last_time=column.find("td",{"class":"regDate last"}).get_text()
        
        writer.writerow([local,company,date,pay,last_time])
        
            
def main():
    inform=requests.get(url)
    inform.raise_for_status()
    
    inform_soup=BeautifulSoup(inform.text,"lxml")
    
    pagination=inform_soup.find("div",{"id":"MainSuperBrand"})
    pages=pagination.find_all("a",{"class":"goodsBox-info"})
    
    for page in pages:
      company=page.find("span",attrs={"class":"company"}).get_text()
      list=page.attrs["href"]
      url_number(list)
      url_load(list,company)
      
      
      
      
     
    
    
main()
