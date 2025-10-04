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

# 배열 만들기 4
def solution6(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    return stk

# 주사위게임 문제
def solution(a, b, c, d):
    nums = [a, b, c, d]
    nums.sort() # 오름차순

    if nums[0] == nums[3]:
        return 1111 * nums[0]
    if nums[0] == nums[2] or nums[1] == nums[3]:
        p = nums[1]
        q = nums[0] if nums[1] != nums[0] else nums[3]
        return (10 * p + q) ** 2
    if nums[0] == nums[1] and nums[2] == nums[3]:
        return (nums[0] + nums[2]) * abs(nums[0] - nums[2])
    if nums[0] == nums[1]:
        return nums[2] * nums[3]
    if nums[1] == nums[2]:
        return nums[0] * nums[3]
    if nums[2] == nums[3]:
        return nums[0] * nums[1]
    return nums[0]
