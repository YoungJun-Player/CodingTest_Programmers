def solution(n):
    answer = []
    a = str(n)
    
    for i in a[::-1]:
        answer.append(int(i))
    return answer