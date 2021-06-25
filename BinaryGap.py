def solution(N):
    xs = bin(N)[2:].strip('0').split('1')
    return max([len(x) for x in xs])
