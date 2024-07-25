def solution(n):
    answer = [n] #초기값 n을 저장
    
    while n > 1: #n이 1보다 클 동안
        if n % 2 ==0: #n이 짝수라면 2를 나눈 값을 저장한다
            n = n // 2
        else: #n이 홀수라면 아래 수식을 실행한 값을 저장한다
            n = 3 * n +1
        answer.append(n)
        
    return answer