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