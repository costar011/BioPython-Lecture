# pandas 란?
# 데이터 프레임(DataFrame) : 데이터 테이블 전체 객체

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