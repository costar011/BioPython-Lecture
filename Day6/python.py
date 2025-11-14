def solution(n_str):
    return str(int(n_str))

def solution(num_list):
    return max(sum(num_list[i] for i in range(0, len(num_list), 2)),
            sum(num_list[i] for i in range(1, len(num_list), 2)))

def solution(rny_string):
    return rny_string.replace('m', 'rn')

def solution(myString, pat):
    return int(pat.lower() in myString.lower())

def solution(names):
    return [names[i] for i in range(0, len(names), 5)]