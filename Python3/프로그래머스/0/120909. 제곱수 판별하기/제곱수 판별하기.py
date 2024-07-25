def solution(n):
    
    for i in range(1,1000001): # 제곱근의 범위를 이빠이 늘림
        if n == i ** 2: # n이 i의 제곱인지 확인
            answer = 1
            break  # 찾으면 바로 브레이크
        else:       
            answer = 2
        
    return answer