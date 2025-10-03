# 더 크게 합치기
def solution1(a, b):
   return int (max(str(a) + str(b), str(b) + str(a)))

######################

# 두 수의 연산값 비교하기
def solution2(a, b):
 return max(int(str(a) + str(b)), 2 * a * b)

######################

#flag에 따라 다른 값 반환하기
def solution3(a, b, flag):
   return  a + b if flag else a - b

######################

# 등차수열
a,d, included = 3, 4, [True, False, False, True, True]
print(a, d, included)

def solution4(a, d, included):
   answer = 0
   for i in range(len(included)):
      print(i, included[i], int(included[i]))
   answer += (a + i * d) * included[i]
   return answer

######################

# 수열
def solution5(arr, queries):
   for i, j in queries:       # queries의 각 [i, j] 꺼내기
      arr[i], arr[j] = arr[j], arr[i]  # 두 값을 교환
   return arr

######################

# 배열 만들기4