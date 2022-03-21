import pandas as pd

#시리즈 구성을 한다 인덱스에 따라 데이터를 나열하므로 딕셔너리 자료형에 가깝다


"""
a 1
b 2
c 3 같은 딕셔너리 자료형에 비슷한다
엑셀과 비슷하다.
"""
#series 란? 시리즈는 인덱스와 값으로 구성됩니다.

"""
딕셔너리

data = {
    'a':'사괴',
    'b':'바나나',    
    'c': '나'
}

print(data)
array=pd.Series(data)
print(array)
print(data['a'])
print(array['a'])
"""

word_dict = {
'Apple': '사과',
'Banana': '바나나',
'Carrot': '당근' }
frequency_dict = {
'Apple': 3,
'Banana': 5,
'Carrot': 7
}
importance_dict = {
'Apple': 3,
'Banana': 2,
'Carrot': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word':word,
    'frequncy' : frequency,
    'importance':importance
})
"""
score = summary['frequncy'] * summary['importance']
summary['score']=score #스코어를 연산해서 넣는 부분
"""
"""
print(summary,'\n')
print(summary.loc['Banana':'Carrot','importance':],'\n') #처음은 열을 기준으로 슬라이싱 한것
#banana carroy 그부분에서 importance 전부를 슬라이싱함 
print(summary.iloc[1:3,2:])
"""
"""
print(summary)

summary.loc['Apple', 'importance']= 5
summary.loc['Elderberry']=['엘더베리',5,3]

print(summary)
"""

summary.to_csv("pandas/summary.csv",encoding="utf-8-sig")
saved=pd.read_csv("pandas/summary.csv",index_col=0)
print(saved)