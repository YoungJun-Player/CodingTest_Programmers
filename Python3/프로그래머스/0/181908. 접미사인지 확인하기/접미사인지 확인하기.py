def solution(my_string, is_suffix):
   
    
    if is_suffix[-1] == my_string[-1] and len(my_string) >= len(is_suffix):
        return 1
    else:
        return 0
    