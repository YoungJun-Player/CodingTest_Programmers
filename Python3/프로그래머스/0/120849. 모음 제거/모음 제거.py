def solution(my_string):
    answer = my_string
    
    for i in my_string:
        if i in "aeiou":
            answer = answer.replace(i, '')
            
    return answer