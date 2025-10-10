 # 캡슐화 사용해야 하는 이유
 # 클래스 인스턴스 내부 데이터 보호하기 위해 사용
 # 클래스 설계할 때 클래스 간 간섭 및 정보 공유 최소화해서 개별 클래스가 단독으로 동작 할 수 있도록 해야함

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age
  def get_age(self): # get 함수
    return self.__age
  def set_age(self, age): # set 함수
    if age <= 0:
      raise ValueError("나이는 0보다 커야 합니다.")
    self.__age = age # 이 줄의 들여쓰기를 수정했습니다.

person = Person("홍길동", 20)
person.set_age(25)
print(person.name)
print(person.get_age())
# print(person.__age)
# 에러 AttributeError: Person object has no attribute __age

 # 캡슐화 사용해야 하는 이유
 # 파이썬에서 지원하는 @property 데코레이터 사용
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    if age <= 0:
      raise ValueError("나이는 0보다 커야 합니다.")
    self.__age = age

person = Person("홍길동", 20)
print(person.age) # 20
# person.age = -1 # 이 줄의 주석을 해제하면 ValueError가 발생합니다.
person.age = person.age - 1
print(person.age) # 19

# 접근제어자 : 변수 선언 방식으로 구분
# _Protected variable : 자기 클래스 내부 혹은 상속받은 자식 클래스에서만 접근 허용
# __Private variable : 자기 클래스 내부의 메서드에서만 접근 허용

# 클래스 : 객체를 만들 수 있는 틀
# 객체: 속성과 메소드 갖는 것

class Calculator:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    return selef.first + self.second
#객체#
my_calculator = Calculator(5,3) #인스턴스#

# 인스턴스 이름(변수 이름) = 클래스 이름()
# 클래스 이름 = 생성자 <- 클래스 이름과 같은 함수가 생성자 라고한다

# 객체와 인스턴스 차이
# my_calculator = Calculator 에서 , my_calculator는 객체 | Calculator는 인스턴스

# class 기반으로 만들어진 객체가 인스턴스임


# 예외
# 예상치 못한 상황이 발생하는 것
# 예측 불가능한 예외 , 예측 가능한 예외

# 조건문으로 사전에 방지
user_input = input("원 반지름을 정수 입력 : ")

if user_input.isdigit():
  number_input = int(user_input)
  print("원의 원지름: ", number_input)
  print("넓이:",(number_input ** 2)* 3.14)
else:
  print("정수를 입력하지 않았습니다")