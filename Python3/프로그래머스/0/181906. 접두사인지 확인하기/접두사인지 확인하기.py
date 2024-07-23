def solution(my_string, is_prefix):

    if is_prefix[0:2] == my_string[0:2] and len(is_prefix) <= len(my_string) :
        return  1
    else:
        return  0