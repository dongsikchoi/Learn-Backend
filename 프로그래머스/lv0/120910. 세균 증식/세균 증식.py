def solution(n, t):
    answer = n 
    for _ in range(t):
        answer = answer * 2
    
    return answer