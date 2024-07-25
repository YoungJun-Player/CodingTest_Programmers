def solution(my_strings, parts):
    
    answer = ''
    
    # my_strings와 parts의 길이는 같으므로 zip 함수를 사용하여 동시에 순회
    for i, j in zip(my_strings, parts):
        
        # part[0]에서 part[1]까지의 부분 문자열을 추출하여 answer에 더함
        # part[1]+1은 Python의 슬라이싱이 끝 범위를 포함하지 않기 때문에 필요
        answer += i[j[0]:j[1]+1]
            
    return answer