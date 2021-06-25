import math
def solution(X, Y, D):
    #X=starting
    #Y=ending
    #D=jumps

    if X==Y:
        return 0
    
    return int(math.ceil((Y-X)/D))          
