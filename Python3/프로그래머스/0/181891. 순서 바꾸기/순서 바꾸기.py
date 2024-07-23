def solution(num_list, n):
    answer = []
    if n == 0:
            answer += num_list[0:]
    else:
            answer += num_list[n:]
            answer += num_list[0:n]
    
    return answer