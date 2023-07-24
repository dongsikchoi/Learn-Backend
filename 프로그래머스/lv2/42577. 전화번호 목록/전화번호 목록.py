def solution(phonebook):
    
    answer = True 
    phonebook.sort()
    
    for arr1, arr2 in zip(phonebook,phonebook[1:]):
        if arr2.startswith(arr1):
            answer = False 
            break 
    
    
    return answer