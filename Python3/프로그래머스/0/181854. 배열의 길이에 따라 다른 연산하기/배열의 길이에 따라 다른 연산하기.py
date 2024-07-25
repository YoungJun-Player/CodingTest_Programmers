def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0 : # arr인덱스의 길이가 짝수라면
        
        for i in range(len(arr)):
            if i % 2 != 0:
                answer.append(arr[i]+n)
            else: 
                answer.append(arr[i])
            
    elif len(arr) % 2 != 0 : #arr인덱스의 길이가 홀수라면
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i]+n)
            else: 
                answer.append(arr[i])
        
    return answer