def solution(phonebook):
    
    hash = {} 
    answer=True
    for num in phonebook:
        hash[num] = ' ' 
    for num in phonebook:
        tmp = ''
        for num_ in num:
            tmp += num_
            if (tmp in hash) and (tmp != num):
                answer=False
                break
    return answer