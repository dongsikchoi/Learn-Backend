def solution(A, B):
    if A==B:
        return 0 
    list_a = list(A)
    list_b = list(B)
    count = 0 
    
    for _ in range(len(A)):
        tmp_list = [] 
        tmp_list.append(list_a[-1])
        for i in range(1,len(A)):
            tmp_list.append(list_a[i-1])
        if tmp_list == list_b:
            count +=1
            return count
        else:
            list_a = tmp_list 
            count +=1
    if count == len(A):
        return -1
    else:
        return count
            
    answer = 0
    return answer