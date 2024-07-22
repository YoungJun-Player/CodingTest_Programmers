def solution(my_string, alp):
    answer = ''
    if alp in my_string:                #만약 alp가 my_string 안에 있다면?
        for i in range(len(my_string)):
            if my_string[i] == alp:
                answer += alp.upper()
            else:
                answer += my_string[i]
        return answer        
    else:                               #alp가 my_string 안에 없으면 원래 값으로 리턴
         return my_string   
            