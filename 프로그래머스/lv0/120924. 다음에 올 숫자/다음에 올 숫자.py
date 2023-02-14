def solution(common):
    if common[-1] - common[-2] == common[-2] - common[-3]:
        return common[-1] + (common[-1] - common[-2])
    elif common[-1] / common[-2] == common[-2] / common[-3]:
        return common[-1] * (common[-1] / common[-2])
    
