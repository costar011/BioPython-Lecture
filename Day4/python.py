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