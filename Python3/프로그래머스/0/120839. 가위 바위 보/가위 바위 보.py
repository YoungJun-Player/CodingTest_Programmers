def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += i.replace(i,"0")
        elif i == "0":
            answer += i.replace(i,"5")
        else:
            answer += i.replace(i,"2")
    return answer