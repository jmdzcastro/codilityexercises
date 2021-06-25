def solution(A, K):
    N=len(A)
    if (N==0):
        return A
        
    shift=K%len(A) #just in case K>length of the array
    
    if (shift==0): #no need to rotate
        return A
        
    arr=A[-shift:]
    arr[shift:]=A[0:N-shift]
    
    return arr
    
