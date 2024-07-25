def solution(price):
    
    if price >= 500000:  # 50만 원 이상일 때 20% 할인
        discount_rate = 0.8
        
    elif price >= 300000:  # 30만 원 이상일 때 10% 할인
        discount_rate = 0.9
        
    elif price >= 100000:  # 10만 원 이상일 때 5% 할인
        discount_rate = 0.95
        
    else:  # 할인이 적용되지 않는 경우
        discount_rate = 1
    
    # 할인된 가격을 계산하고 소수점 이하를 버린 정수로 반환
    answer = int(price * discount_rate)
    
    return answer