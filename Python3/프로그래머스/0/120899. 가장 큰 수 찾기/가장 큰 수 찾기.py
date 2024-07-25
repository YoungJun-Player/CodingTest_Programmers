def solution(array):
    
    array_max = max(array)
    
    for i in range(len(array)):
        if array[i] == array_max:
            answer = [array_max,i]
    
    return answer