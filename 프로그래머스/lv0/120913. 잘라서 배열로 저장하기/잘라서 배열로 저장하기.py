def solution(my_str, n):
    answer = []
    div = len(my_str) // n 
    count = 0 
    for i in range(div):
        tmp = my_str[(n*i):(n*(i+1))]
        answer.append(tmp)
        count += 1 
        
    if len(my_str) % n != 0:
        
        answer.append(my_str[(n*count):-1]+my_str[-1])
    else:
        pass
    return answer