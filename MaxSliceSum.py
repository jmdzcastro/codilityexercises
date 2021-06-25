from itertools import accumulate

def solution(A):
    pref=list(accumulate(A))
    #print(pref)
    n = len(A)
    result = 0
    for p in range(n):
        for q in range(p+1, n):
            sum1 = pref[q] - pref[p]
            result = max(result, sum1)   
    return result
