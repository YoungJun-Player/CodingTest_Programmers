def solution(num_list):
    answer = 0
    one = 0
    two = 0
    
    for i in range(len(num_list)):
        if i % 2 ==0:
            one += num_list[i]
        else:
            two += num_list[i]
            
    if one > two:
        answer = one
    elif one < two:
        answer = two
    else:
        answer = one
        
    return answer