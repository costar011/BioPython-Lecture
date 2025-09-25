# Docstring 독스트링은 함수, 클래스, 모듈에 포함할 수 있는 도큐먼테이션으로 이들의 목적과 이용할 때 필요한 세부 정보를 담는데 활용

def sum(a,b) -> float:
  """
  이 함수는 입력값 a와 b를 더해주는 함수

  입력: a,b
  결과: a + b
  """

  return float(a) + float(b)

print(sum.__doc__)

# count() - 문자열 길이 반환
a = "happy"
a.count("p")

# find() - 지정한 문자가 처음 나온 위치 반환, 문자나 문자열 없으면 -1 반환
# rfind() - 오른쪽부터 찾음
#  <-

a = "happy"
a.find("p")

#  -1 반환
a = "happy"
a.find("b")

# join() - 문자 사이에 지정한 문자 삽입
a = "happy"
",".join(a)

# lstrip() - 왼쪽 공백 지우기
# rstrip() - 오른쪽 공백 지우기
# strip() - 양쪽 공백 지우기

a = " Happy "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# replace() - 문자열 바꾸기
# replace(바뀔 문자열, 바꿀 문자열)

a = "happy"
a.replace("y", "end")

# split() - 문자열 나누기
# split() 기본 설정은 공백 기준, 반환되는 값은 리스트 자료형으로 반환
a = "Happy1Happy2Happy3"
a.split("Happy1Happy2Happy3")

# 리스트 자료형 = 배열
# 하나의 변수에 여러 개의 값을 저장, 인덱스로 접근
# 대괄호로 감싸주고 요소값은 , 로 구분

a = []
a = list()
b = [1,2,3]
c = ["Happy", 2025]
print(a)
print(b)
print(c, type(c), type(c[0]), type(c[1]))

# 중첩 리스트 - 배열과 같은 문법으로 중첩 리스트 사용이 가능
a = [1,2,3,["a","b","c"]]
print(a[0])
print(a[3])

# 2차열 배열
print(a[3][2])

# 리스트 슬라이싱 - list도 슬라이싱 가능, 슬라이싱 간격도 지정 가능
# 변수명[시작 인덱스:마지막 인덱스:간격]

lst = [1,2,3,4,5,6] # lst라는 이름의 리스트를 생성하고, 1부터 6까지의 정수를 요소로 저장
print(lst[1:2])
# 리스트 lst를 슬라이싱 시작 인덱스는 1이고 마지막 인덱스는 2
# 인덱스 1에 해당하는 요소만 가져옴,  lst의 인덱스 1은 2이므로 결과는 [2]가 출력
print(lst[:2])
# 시작 인덱스를 생략하고 마지막 인덱스를 2로 지정하여 슬라이싱
# 시작 인덱스가 생략되면 리스트의 처음부터 시작
# 인덱스 2 전까지의 요소, 즉 인덱스 0과 1에 해당하는 요소들을 가져옴, lst의 인덱스 0은 1, 인덱스 1은 2이므로 결과는 [1, 2]가 출력
print(lst[2:])
# 시작 인덱스를 2로 지정하고 마지막 인덱스를 생략하여 슬라이싱
# 인덱스 2부터 리스트의 끝까지의 요소들을 가져옴, lst의 인덱스 2는 3이고 그 이후 요소들은 4, 5, 6이므로 결과는 [3, 4, 5, 6]가 출력

print("==========================")
lst = [1,2,3,4,5,6]
print(lst[::2])
print(lst[:5:2])
print(lst[::-1])


# list 연산, 길이, 포함 여부
# 연산자를 사용해서 리스트 다룰 수 있음
# 리스트 합치기(+), 반복하기(*), 리스트에 값이 포함됐는지 여부 -> in
# len() 함수를 사용해서 리스트의 길이를 구할 수 있음

a = [1,2,3]
b = [4,5,6]
print(a + b)

print("==========================")

a = [1,2,3]
print(a * 2)

print("==========================")

a = [1, 2, 3, ["a", "b"], "c"]
print(len(a))
print(len(a[3]))

print("c" in a)

print("==========================")

# list 수정,삭제
# index로 접근해서 수정, 삭제 가능
# del()  함수 사용해서 리스트 요소값 삭제 가능
a = [1, 2, 3, ["a", "b"], "c"]
a[4] = "d"
print(a)

del a[4]
print(a)

print("==========================")
a = [1, 2, 3, ["a", "b"], "c"]
a[3][1] = "c"
print(a)

print("==========================")


# 리스트 변수명 뒤에 . 붙여 어려가지 리스트 관련 함수를 사용할 수 있음
# append()
a = [1,2,3]
a.append(4)
print(a)

print("==========================")

# extend()
a = [1,2,3]
b = [3,4,5]
a.extend(b)
print(a)

print("==========================")

# sort()
a = [3,2,1]
print(a)
a.sort()
print(a)

print("==========================")

# sort() 와 sorted() 비교
# sort() - 기존 리스트 변경하고 return 없음
# sorted() - 기존 리스트 변경 X , 정렬된 리스트 반환
a = [3, 2, 1]
print(a)
print("Sort() :", a.sort())
print(a)


print("==========================")


a = [3, 2, 1]
print(a)
print("Sorted() :", sorted(a))
print(a)

# 튜플 자료형- = 값이 변하지 않는 배열
# 튜플은 ()로 선언
# 튜플은 요소값을 바꿀 수 없어서 삽입, 삭제, 수정이 안됨
# 단 1개의 요소만을 가질때도 반드시 요소 뒤에 , 를 넣어줘야함
# 소괄호 생략 가능

t1 = ()
t2 = tuple()
print(type(t1))
print(type(t2))

print("==========================")

# 집합(set) 자료형 - = 중복을 허용하지 않고 순서가 없는 배열
# 순서가 없으므로 인덱싱을 사용해서 접근할 수 없음
# 중복 허용하지 않음, 튜플과 다르게 값을 추가 / 삭제 / 갱신 할 수 있음
# 집합 연산자를 지원함 ( union, intersection, minus 등)
# 순서가 없으므로 인덱싱을 사용해서 접근 할 수 없음

s1 = set([1,2,3])
print(type(s1))
print(s1)

print("==========================")

s2 = ([1,2,3])
print(type(s2))
print(s2)
print("==========================")

# 교집합 intersection() 함수
# 두 집합 양쪽에 모두 포함된 값만 추출하는 연산

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

print("==========================")

# 딕셔너리 자료형 - key-value 자료형
# 순차적으로 값을 구하지 않고 key로 value를 리턴함
# 딕셔너리변수명 = {key1:value1, key2:value2, key3:value3}

dic1 = {}
dic2 = dict()
print(type(dic1))
print(type(dic2))

print("==========================")

# 딕셔너리 자체 함수
# keys() 함수 - Key만 모아서 dict_keys 객체 리턴
# values() 함수 - Value만 모아서 dict_values 객체 리턴
# items() 함수 - key와 value 쌍을 묶은 값을 dict_items 객체 리턴
# clear() 함수 - key-value 모두 지움 get(x) 함수 - X 라는 key에 대응되는 value 리턴
a = {"name":"costar", "year":2025, "student_number":"25510001"}
print(a.keys())
print(a.values())
print(a.items())
print(a.get("name"))

print("==========================")

# 조건부 표현식
score = 99
if score >= 60:
  message = "success"
else:
  message = "fail"
print(message)

print("==========================")

score = 99
message = "success" if score >= 60 else "fail"
print(message)

print("==========================")

num = 99
rs = "짝수" if num % 2 == 0 else "홀수"
print(rs)

print("==========================")


# while 문 - 주어진 조건이 true 인 경우 명령 문장을 수행하고 false인 경우 반복 중단
# continue문은 남은 명령 문장을 건너 뛰고 다시 조건문으로 돌아감
# brak 문은 반복문 강제 종류
score = 95
while score < 100:
  score += 1
  if score == 97:
    break
  print(score)

# for문 사용
# 리스트 탐색 하면서 변수 언패킹 하는 경우

test = [[1,2],[3,4],[5,6]]
for(left, right) in test:
  print(left, right)


# 패킹과 언패킹
# 변수 만드는 방법은 여러가지이며 패킹과 언패킹 구분이 가능함

a,b = ("python", "hi")
print(a,b)
(a,b) = "python", "hi"
print(a,b)

print("==========================")

test = (1,2,3,4)
print(test)
a,b,c,d = test
print(a,b,c,d)

# range() 함수 - 리스트 만들어주는 함수
# range(시작 숫자, 종료 숫자) 함수와 for문을 같이 사용함
test = range(2,10)
print(test)
print(type(test))

# 구구단
for i in range(2,10):
  print(f"{i}단")
  for j in range(1,10):
    print(f"{i} * {j} = {i * j}")