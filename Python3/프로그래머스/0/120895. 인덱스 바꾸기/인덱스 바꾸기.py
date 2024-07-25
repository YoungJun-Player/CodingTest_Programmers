def solution(my_string, num1, num2):
    answer = ""
    # 문자열을 리스트로 변환
    string_list = list(my_string)
    
    # 두 인덱스의 문자를 서로 바꿈
    string_list[num1], string_list[num2] = string_list[num2], string_list[num1]
    
    # 리스트를 문자열로 변환하여 반환
    return answer.join(string_list)