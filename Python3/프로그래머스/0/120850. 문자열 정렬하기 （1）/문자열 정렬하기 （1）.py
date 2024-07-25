import re

def solution(my_string):
    answer =[]
    a=re.findall('\d',my_string)
    for i in a:
        answer.append(int(i))
    return sorted(answer)