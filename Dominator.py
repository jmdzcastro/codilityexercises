def solution(A):
    B=A.copy()
    B.sort()
    
    if len(A)==0:
        return -1
        
    candidate=B[len(B)//2]

    if len([number for number in A if number == candidate]) <= len(A)//2:
        return -1

    return A.index(candidate)
