
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