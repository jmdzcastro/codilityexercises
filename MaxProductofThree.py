def solution(A):
    if len(A)==3:
        return(A[0]*A[1]*A[2])
    A.sort()

    if len(A)>=6:
        biggest=A[0:3] #only need 2 negative values to create positive
        biggest[4:]=A[-3:]
    else:
        biggest=A
    
    result=biggest[0]*biggest[1]*biggest[2] #temp max
    
    for x in range(len(biggest)):
        for y in range(x+1,len(biggest)):
            for z in range(y+1,len(biggest)):
                if biggest[x]*biggest[y]*biggest[z]>result:
                    result=biggest[x]*biggest[y]*biggest[z]
    return result   
