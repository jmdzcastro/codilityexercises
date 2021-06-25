def solution(A):
    if len(A)!=max(A):
        return 0
    A.sort()
    
    B=[i for i in range(1,len(A)+1)]
    if (A==B):
        return 1
    
    return 0    
