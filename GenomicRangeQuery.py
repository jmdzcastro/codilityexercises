def solution(S, P, Q):
    result=[]
    for i in range(len(P)):
        if "A" in S[P[i]:Q[i]+1]:
            result.append(1)
        elif "G" in S[P[i]:Q[i]+1]:
            result.append(2)
        elif "C" in S[P[i]:Q[i]+1]:
            result.append(3)
        else:
            result.append(4)
    return result
    
