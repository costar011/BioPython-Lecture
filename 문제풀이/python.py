# 더 크게 합치기
def solution1(a, b):
 return int (max(str(a) + str(b), str(b) + str(a)))


# 두 수의 연산값 비교하기
def solution2(a, b):
 return max(int(str(a) + str(b)), 2 * a * b)