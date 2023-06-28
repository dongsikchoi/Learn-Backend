num=int(input())
count =0
for _ in range(num):
    word = input()
    tmp_hash = dict() 
    
    is_group = True
    for i in range(len(word)):
        
        if word[i] not in tmp_hash:
            tmp_hash[word[i]] = 0 
        else:
            if ( i > 0 ) and ( word[i-1] != word[i] ):
                if word[i] in tmp_hash:
                    is_group = False 
                    break 
            else:
                tmp_hash[word[i]] += 1
    if is_group:
        count += 1 
print(count)