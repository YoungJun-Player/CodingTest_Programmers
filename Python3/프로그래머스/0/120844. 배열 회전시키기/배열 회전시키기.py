def solution(numbers, direction):
    answer = []

    if(direction == "right"):
        answer = numbers[-1:] + numbers[0:len(numbers)-1]
    if(direction == "left"):
        answer = numbers[1:len(numbers)+1] + numbers[0:1]

    return answer