import re

def solution(my_string):
    answer = 0
    a = re.sub(r"[a-z]","",my_string)
    b = re.sub(r"[A-Z]","",a)
    # answer = re.sub(r"[A-Z]","",my_string)
    
    for i in range(len(b)):
        answer += int(b[i])

    return answer