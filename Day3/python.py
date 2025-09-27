
# 패킹 : 변수에 여러개 데이터 할당하는 자체가 리스트
# 언패킹 : 여러개 데이터가 들어있을 때 각 변수로 반환

t = [1,2,3] # 1 2 3 을 변수 t에 패킹
a,b,c = t # t 있는 값 1 2 3 을 변수 a b c 에 언패킹

print(a,b,c) # 값은 1,2,3 이 나옴

list_of = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]
print(list_of)

print("===========")

print(list_of[0][1]) # 2
print(list_of[1][3]) # 7
print(list_of[2][1]) # 9
print("===========")

indices = [(0, 1), (1, 3), (2, 1)]

for i, j in indices:
    print(list_of[i][j])

print("===========")

for items in list_of:
  print(items)



 # 계산기 클래스 만들기
class Calculator:
  def __init__(self, first, second): # __init__ : 예약 함수
    self.result = 0
    self.operator = ""
    self.first = first
    self.second = second

  def __str__(self):
    return f'{self.first} {self.operator} {self.second} = {self.result}'

  def set_data(self, first, second):
    self.first = first
    self.second = second

  def get_result(self):
    return f"{self.first} {self.operator} {self.second} = {self.result}"

  def add(self):
    self.result = self.first + self.second
    self.operator = "+"
    return self.result

  def sub(self):
    self.result = self.first - self.second
    self.operator = "-"
    return self.result

  def mul(self):
    self.result = self.first * self.second
    self.operator = "*"
    return self.result

  def div(self):
    self.operator = "/"
    self.result = self.first / self.second
    return self.result

  cal = Calculator(5,3)
  print(cal.first) # 5
  print("===========")

  cal.add()
  print(cal.get_result()) # 5 + 3 = 8
  print("===========")

  cal.set_data(10,20)
  print(cal.get_result()) # 10 + 20 = 8
  print(cal.operator)
  print("===========")

  # 클래스 상속해서 계산기 확장
class MoreCalculator(Calculator):
  def __init__(self, first, second):
    super().__init__(first, second)

  def pow(self):
    self.operator = "**"
    self.result = self.first ** self.second
    return self.result

  def div(self):
    self.operator = "/"
    self.result = 0 if self.second == 0 else self.first / self.second
    return self.result

  cal = MoreCalculator(5,3)
  print(cal.pow())
  print(cal.get_result())
  cal.add()
  print(cal.get_result())


# 다형성 - 같은 이름의 메소드가 다른 기능을 하는 것
class animal:
  def __init__(self, name):
    self.name = name
  def talk(self):
    raise NotImplementedError("subclass must implement abstract method")

class cat(animal):
  def talk(self):
    return "meow"

class dog(animal):
  def talk(self):
    return "woof"

  animals = [cat("야옹이"), dog("멍멍이")]
  for animal in animals:
    print(animal.name + ": " + animal.talk())