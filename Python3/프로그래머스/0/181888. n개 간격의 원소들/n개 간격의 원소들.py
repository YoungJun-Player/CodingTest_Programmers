def solution(num_list, n):
    answer = []
    
    # answer리스트에 num_list 인덱스를 n개 간격으로 리턴
    answer += num_list[::n]
    
    return answer