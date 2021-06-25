def solution(A):
    if max(A)<=0:
        return 1
    
    for i in range(1,max(A)+2):
        if i not in A:
            return i
