def solution(num_list):
    answer = 0
    a = 1
    for i in range(len(num_list)):
        if len(num_list) >= 11:
            answer += num_list[i]
        else:
            a *= num_list[i]
            answer = a
    return answer