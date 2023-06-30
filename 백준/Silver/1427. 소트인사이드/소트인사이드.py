num = input()
num_hash = dict() 
for digit in num:
    if digit in num_hash: 
        num_hash[digit] += 1 
    else:
        num_hash[digit] = 1 
answer = ''
for num in range(9,-1,-1):
    if str(num) in num_hash: 
        answer += str(num) * num_hash[str(num)]
print(answer)