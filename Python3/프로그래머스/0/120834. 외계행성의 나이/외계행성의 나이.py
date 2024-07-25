import string

def solution(age):
    answer = ""
    list_lower = list(string.ascii_lowercase) # 알파벳 나열 
    
    for i in range(len(str(age))):
        answer += list_lower[int(str(age)[i])]
    return answer