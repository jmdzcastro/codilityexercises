def solution(A):
    west=[i for i in range(len(A)) if A[i]==0] #discovers the 0s position
   
    pairs=0
    ctr=len(west)
    for i in range(len(west)):
        pairs+=len(A)-west[i]-ctr
        #print("{}={}-{}-{}" .format(pairs,len(A),west[i],ctr))
        ctr-=1
        if pairs>1000000000:
            return -1
    return pairs
