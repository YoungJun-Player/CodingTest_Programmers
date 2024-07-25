def solution(n, k):
    n_1 = (n//10)*2000
    # k_1 = (10*n) // 10 
    answer = n*12000+k*2000 -n_1
    return answer