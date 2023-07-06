num = input()
result = [0]*10

for i in range(len(num)):
    tmp_num = int(num[i])
    if tmp_num == 6 or tmp_num == 9:
        if result[6] == result[9]:
            result[6] += 1
        else:
            result[9] += 1 
    else: 
        result[tmp_num] += 1 
print(max(result))