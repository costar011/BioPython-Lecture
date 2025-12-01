# 7
def solution1(order):
    return sum([5000 if "cafelatte" in i else 4500 for i in order])

# 8
def solution(arr, k):
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
        if len(result) == k:
            break
    return result + [-1] * (k - len(result))

# 9
def solution3(arr, query):
    for i in range(len(query)):
        q = query[i]
        
        if i % 2 == 0:
            arr = arr[:q + 1]
            
        else:
            arr = arr[q:]
            
    return arr

# 10
def solution(code):
    ret = ""
    mode = 0 # mode는 0에서 시작
    
    for idx, char in enumerate(code):
        if mode == 0:
            if char != "1":
                if idx % 2 == 0:
                    ret += char
            else:
                mode = 1
                
        elif mode == 1:
            if char != "1":
                if idx % 2 != 0:
                    ret += char
            else:
                mode = 0
    # 최종 ret이 빈 문자열이면 "EMPTY"를 반환하고, 아니면 ret을 반환        
    if not ret:
        return "EMPTY"
    else:
        return ret

# 11
def solution(board, k):
    total_sum = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            if i + j <= k:
                total_sum += board[i][j]
                
    return total_sum