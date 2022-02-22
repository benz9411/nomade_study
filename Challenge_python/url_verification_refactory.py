import os
import requests


def clear():
  os.system('clear')

while True:
  print("Welcome to IsItDown.py")
  print("please write a URLs you want to check. (separated by comma)")
  urls=input().lower().split(",")
  # 첫번째 이 url 이 정상적인 url 인가?
  for url in urls:
    url=url.strip()
    if url.find('.')==-1:
      print(url+"is not a valid URL")
      continue  
    else: 
      if url.find("http") and url.find("https") == -1:
          url="http://"+url[0:]
      try:
        url_result=requests.get(f"{url}")
        if url_result.status_code == 200:
            print(f"{url} is up")
        elif url_result.status_code == 404:
            print(f"{url} is down")
      except requests.exceptions.RequestException: #아에 존재하지 않는 url이 입력 
          print(f"{url} is down")
  repeat=input("Do you want to start over? y/n ")
  if repeat=='y':
    clear()
  elif repeat=='n':
    print("k, bye")
    break
  else:
    a=True
    while True:
      print("That's not a valid answer")
      repeat=input("Do you want to start over? y/n ")
      if repeat=='y':
        break
      elif repeat=='n':
        a=False
        print("k, bye")
        break
    if a:
      clear()
      continue
    else:
      break

            
        
  