# def solution(a, b):
#     a = int(str(a)+str(b))
#     b = 2*a*b
    
#     if a >= b:
#         return a
    
#     else:
#         return b
    
def solution(a, b):
    return max(int(f"{a}{b}"), 2*a*b)
