import math
def solution(N):
    if N==1:
        return 1
    
    ctr=0
    last=int(math.sqrt(N))
    for i in range(1,last+1):
        if N%i==0:
            ctr+=2

    if N%math.sqrt(N)==0:
        ctr-=1
    return ctr
