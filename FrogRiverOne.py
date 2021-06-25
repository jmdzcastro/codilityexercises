def solution(X, A):
    leaf_tracker=[]

    for index, leaf in enumerate(A):
        if leaf not in leaf_tracker:
            leaf_tracker.append(leaf)
            if len(leaf_tracker)==X:
                return index
    return -1
