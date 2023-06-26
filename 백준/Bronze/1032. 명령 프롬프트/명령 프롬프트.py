import sys 
num = int(input())
result = ''
for _ in range(num):
    input_ = list(input())
    if not result: 
        result = input_ 
    else: 
        for i in range(len(input_)): 
            if result[i] != '?' and result[i] !=  input_[i]:
                result[i] = '?'

print(''.join(result))