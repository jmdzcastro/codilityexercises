def solution(S):
    if len(S)%2!=0:
        return 0
    if S=='':
        return 1
    matches, stack = dict(['()', '[]', '{}']), []

    for i in S:
        if i in matches.values():
            if stack and matches[stack[-1]] == i:
                stack.pop()
            else:
                return 0
        else:
            stack.append(i)
    if len(stack)==0:
        return 1
    return 0
