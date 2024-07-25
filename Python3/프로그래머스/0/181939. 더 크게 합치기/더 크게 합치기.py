def solution(a, b):
    
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    
    if ba > ab:
        answer = ba
    else:
        answer = ab
        
    return answer