def solution(arr):
    answer = []  
    for i in arr: # arr의 각 원소 i를 answer 배열에 추가합니다.
        for j in range(i): #j를 i개수만큼 반복
            answer.append(i)
    return answer