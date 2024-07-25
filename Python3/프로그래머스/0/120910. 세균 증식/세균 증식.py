def solution(n, t):
    answer = [n]

    for i in range(t):
        answer.append(answer[i]*2)
    return answer[-1]

print(solution(7,15))