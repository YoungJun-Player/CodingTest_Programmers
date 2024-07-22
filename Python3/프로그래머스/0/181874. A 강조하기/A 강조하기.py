def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] == "a":      #a라면 A로 바꾼다
            answer += "A"
        
        elif myString[i].isupper() and myString[i] != "A":     #대문자면 소문자로 바꾼다
            answer += myString[i].lower()
            
        else:     #띄어쓰기거나, 소문자면 그대로 넣는다
            answer += myString[i]
            
    return answer