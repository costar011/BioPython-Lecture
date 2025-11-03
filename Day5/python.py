# pandas 란?
# 데이터 프레임(DataFrame) : 데이터 테이블 전체 객체
# 파이썬을 이용한 데이터 분석 및 조작 라이브러리
# 시리즈(Series): 단일 열이나 행을 나타내는 자료구조로, 데이터프레임의 한 부분이며, 인덱스와 값으로 구성
# 데이터 입출력: 다양한 형식의 데이터를 읽고 쓸 수 있는 기능을 제공  CSV, Excel, SQL, JSON 등 다양한 형식을 지원
# 데이터 조작 및 변환: 데이터프레임을 이용하여 데이터 조작, 변환, 병합, 결합 등 다양한 작업을 수행

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

list_data = [1,2,3,4,5]
list_name = ["a","b","c","d","e"]
example_ob = Series(data = list_data, index = list_name)
example_ob

##########################

dict_data = {"a":1, "b":2, "c":3, "d":4, "e":5} # key값 중복 안됨
example_obj = Series(dict_data, dtype=np.float32, name="example_data")
example_obj

##########################
raw_data = {"이름": ["홍길동", "김철수","이영희"], "나이":[22, 21, 20], "지역":["대전", "서울", "청주"], "취미":["코딩","독서","게임"]}
df = pd.DataFrame(raw_data, columns=["이름", "나이", "지역","취미"])
df

##########################
df = pd.read_excel("sample_data.xlsx")
df

##########################

df.head(4).T # 엑셀에서 행렬바꿈

##########################

df.index = df["주민등록번호"] # index 지정 (주민등록번호)
df


##########################

df.loc[["430905-1436086"],["이름", "핸드폰번호"]]


##########################

df.drop(1).head() # 데이터프레임에 드랍하고 행 출력

##########################

df = pd.read_excel("groupby.xlsx")
df

##########################
df.groupby("반")["점수"].sum()

##########################
mt_groupby = df.groupby(["반","년도"])["점수"].sum()
mt_groupby

##########################

# Data Frame 정의하기
data = {'name':['Jeong','Lee','Choi','Kim','Hong'],
        'age':[21, 22, 23, 24, 25 ],
        'stamp':[11.0, 12.0, 13.5, 14.5, 15]
        }
df = pd.DataFrame(data)
# Data Frame을 사용하면 가독성이 좋은 행과 열의 구조를 가진 데이터로 변형
df

##########################