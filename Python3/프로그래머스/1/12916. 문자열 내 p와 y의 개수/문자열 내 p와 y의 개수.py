def solution(s):
    answer = []
    answer_1 = []
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in s:
        if i =='p':
            answer += 'p'
        elif i == 'P':
            answer += 'P'
        elif i == 'y':
            answer_1 += 'y'
        elif i == 'Y':
            answer_1 += 'Y'
    
    if len(answer) == len(answer_1):
        return True
    else: 
        return False
    
    if 'p'or 'P'or 'y'or'Y' in s:
        return True