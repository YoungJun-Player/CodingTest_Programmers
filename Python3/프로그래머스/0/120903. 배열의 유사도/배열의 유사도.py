def solution(s1, s2):
    
    s_1 = set(s1)
    s_2 = set(s2)
    
    answer = s_1.intersection(s_2)
            
            
    return len(answer)