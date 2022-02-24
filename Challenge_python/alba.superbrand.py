import requests
import re

print("Welcome to IsItDown.py")
print("please write a URLs you want to check. (separated by comma)")


def url_plus(string):
  plus=string[0:7]
  if plus not in  'https://':
    return True
  
def url_reading(string): #url이 정상인지 판단
  p = re.compile('^(https?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')
  if(p.match(string) != None):
    return True
  else:
    return print(f"{string} is not a valid URL")
  
while True:
  urls=input().strip().split(',')  #url을 컴마와 공백을 삭제
  for url in urls:  #자른 공백 문자열을 for 문으로 확인
     URL=url
     url_result=url
     if url_result.status_code == 200:
          print(f"{URL} is up")
     elif url_result.status_code == 404:
          try:
            url_result=requests.get(f"{URL}")
            url_result.raise_for_status()
          except requests.exceptions.RequestException:
             print(f"{URL} is down")
             continue
     if url_plus(URL):
       URL="https//:"+URL[0:]  
     if url_reading(URL):
    
      
      try:
          url_result=requests.get(f"{URL}")
      except requests.exceptions.RequestException:
           print(f"{URL} is down")
           continue
              
    
    #일단 URL 분리 후 예외 처리까지 완료
    #404 확인이랑 앞에 http 확인, 무한 반복문 까지 해결하면 완료