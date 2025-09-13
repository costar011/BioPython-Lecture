
# 파이썬은 주석을 쓸 때 # 을 쓰면 됨
# 주석은 코드에 대한 설명을 적는 것


"hello world"

print("==================================================================")

# 파이썬 자료형

# 정수형 (int)
# 양의 정수, 음의 정수, 0을 포함
a = 10
b = -5
c = 0

# 2진수 (Binary)
# 0b 또는 0B 접두사를 사용
binary_num = 0b1011 # 11 (십진수)

# 8진수 (Octal)
# 0o 또는 0O 접두사를 사용
octal_num = 0o13 # 11 (십진수)

# 16진수 (Hexadecimal)
# 0x 또는 0X 접두사를 사용
hex_num = 0xA # 10 (십진수)


# 실수형 (float)
# 소수점이 있는 숫자를 표현
d = 3.14
e = -2.718

# 복소수형 (complex)
# 실수부와 허수부를 가짐
# j 또는 J를 사용하여 허수부를 나타냄
f = 1 + 2j
g = -3j

# 문자열형 (str)
# 작은따옴표(')나 큰따옴표(")로 묶어서 표현
h = "안녕하세요"
i = 'Python'

# 불리언형 (bool)
# True 또는 False 값을 가짐
j = True
k = False

# 각 자료형의 값을 출력하여 확인
print(f"정수형: a={a}, b={b}, c={c}")
print(f"2진수: binary_num={binary_num}")
print(f"8진수: octal_num={octal_num}")
print(f"16진수: hex_num={hex_num}")
print(f"실수형: d={d}, e={e}")
print(f"복소수형: f={f}, g={g}")
print(f"문자열형: h='{h}', i='{i}'")
print(f"불리언형: j={j}, k={k}")

print("==================================================================")

a = "hello world"
b = 'hello world'
print(type(a), type(b))
print(a)
print(b)

print("==================================================================")

# 파이썬 연산

# 문자
head = "python"
tail = "is fun"
print(head + tail)

print(tail * 2)

# 숫자
a = "python"
print(a * 2)

print("==================================================================")

#  파이썬 인덱싱과 슬라이싱

a = "Python is fun"
# Python is fun
# a[-1] 은 맨 끝을 말하는 것
print(a[3], a[-1])

b = "Python Love"
print(b[2], b[-1])

print("==================================================================")

# 파이썬 참, 거짓
if True:
  print("이 문장은 항상 실행")
if False:
  print("이 문장은 실행되지 않음")

x = 10
if x > 5:  # x > 5는 True를 반환
  print("x는 5보다 큽니다.")

# 형변환
# 자료형 변환은 float 함수나 int 함수사용하면 간단히 변환 가능
# 파이썬에서는 int 함수 사용하면 내림이 발생함 ( int() 함수는 정수로 변환하는 함수인데, 실수(float)을 int()로 변환하면 소수점 아래 부분이 버려지게 되는데 이걸 '내림'이라고 하는데 반올림 이랑은 다른거임 )

# 실수를 정수로 변환할 때 int() 사용
float_num = 3.14
int_num = int(float_num)
print(f"실수 {float_num}을 int()로 변환: {int_num}")

float_num_2 = 45.66
int_num_2 = int(float_num_2)
print(f"실수 {float_num_2}을 int()로 변환: {int_num_2}")

# format 함수를 이용한 포맷팅
# 내장 함수 format 이용할 수 있고 문자열 내 문자가 나타날 위치를 { } 로 지정
text = "이름"
name = "코딩"

print("{}은 {} 이다 ".format(text, name))

print("==================================================================")

year = 2003
print(f"{2025 - year}살 ")
print( type(year))

print("==================================================================")