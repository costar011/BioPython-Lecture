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