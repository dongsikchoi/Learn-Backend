import sys
a_num = int(sys.stdin.readline())
a_list = list(map(int,sys.stdin.readline().split()))
b_num = int(sys.stdin.readline())
b_list = list(map(int,sys.stdin.readline().split()))

hash = {} 

for num in a_list:
    if num in hash:
        hash[num] += 1 
    else:
        hash[num] = 1 
for num in b_list:
    if num in hash:
        print(hash[num],end= ' ')
    else:
        print(0, end= ' ')
