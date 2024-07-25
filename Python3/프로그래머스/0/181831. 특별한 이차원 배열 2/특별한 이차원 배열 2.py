def solution(arr):
    
    for i in range(len(arr)): #조건 만족하는게 디폴트값
        for j in range(len(arr)):
    
            if arr[i][j] != arr[j][i]: #만약 다른 경우에만 0 리턴
                return 0   
    return 1
