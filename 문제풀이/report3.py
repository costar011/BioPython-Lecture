# 1
def solution1(order):
    return sum([5000 if "cafelatte" in i else 4500 for i in order])

# 2
def solution(arr, k):
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
        if len(result) == k:
            break
    return result + [-1] * (k - len(result))