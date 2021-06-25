def solution(N, A):
    
    flag=[0]*N

    for i in A:
        if i==N+1:
            flag=[max(flag)]*N
        else:
            flag[i-1]+=1
    
    return flag
