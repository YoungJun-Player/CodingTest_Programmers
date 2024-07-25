def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    a = str(n)
    
    for i in range(len(a)):
        answer+=int(a[i])
    
    return answer