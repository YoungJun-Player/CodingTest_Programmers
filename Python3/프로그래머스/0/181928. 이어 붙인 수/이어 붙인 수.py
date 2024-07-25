def solution(num_list):
    answer = ""
    answerr = ""
    
    for i in num_list:
        if i % 2 ==0:
            answer += str(i)
        else:
            answerr+=str(i)
            
    answerrr =  int(answer) + int(answerr)
        
            
    
    return answerrr