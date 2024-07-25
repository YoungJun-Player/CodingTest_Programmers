def solution(num_list):
    answer = 0
    answer_1 = 1
    answer_2 = sum(num_list)**2
    
    for i in num_list:
        answer_1 *= i
        
    if answer_1 > answer_2:
        return 0
    elif answer_1 < answer_2:
        return 1
   