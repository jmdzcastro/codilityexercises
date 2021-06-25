def solution(A, B, K):
   ctr=0

   for i in range(A,B+1):
       if i%K==0:
           ctr+=1
    
   return ctr
