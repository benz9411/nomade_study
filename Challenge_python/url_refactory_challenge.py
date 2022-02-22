import os
import requests


def clear():
  os.system('clear')
  
def restart():
  repeat=str(input("Do you want to start over? y/n ")).lower()
  if repeat=='y' or repeat == 'n':
    if repeat == 'n':
      print("k, bye")
      return  # 특정 조건일때 함수를 중간에 빠져나오게 하는 문 n이 입력되서 그냥 함수가 나옴
    elif repeat=='y':
      main()
  else:
    print("That's not a valid answer")
    restart()

#while True: 좀 더 간결한 코드를 위한 main 함수 생성 => 
def main():
  clear()
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
    restart()     #
    
    
main() #보완점 1.함수 2개를 사용해서 간단한 코드 구현 
          #   2.반복문에서 while True를 빠저나가기 위해 생각을 너무 많이씀 => 코드가 더러워지고 이해하기 힘들어짐 => def restart()로 조건 불만족시 재귀를 돌리는 방법 채택
          #
        
        
          
    
  # 리팩토링 주석    
  # repeat=input("Do you want to start over? y/n ")
  # if repeat=='y':
  #   clear()
  # elif repeat=='n':
  #   print("k, bye")
  #   break
  # else:
  #   a=True
  #   while True:
  #     print("That's not a valid answer")
  #     repeat=input("Do you want to start over? y/n ")
  #     if repeat=='y':
  #       break
  #     elif repeat=='n':
  #       a=False
  #       print("k, bye")
  #       break
  #   if a:
  #     clear()
  #     continue
  #   else:
  #     break
