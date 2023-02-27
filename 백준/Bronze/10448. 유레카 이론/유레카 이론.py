import sys 

num = int(sys.stdin.readline().strip())

hash = dict()

tri_num = []
for i in range(1,45):
    tri_num.append(i * (i + 1) // 2)

for i in tri_num:
    for j in tri_num:
        for k in tri_num:
            tmp = i + j + k 
            if tmp <= 1000:
                hash[tmp] = ''
for _ in range(num):
    input = int(sys.stdin.readline().strip())
    if input in hash:
        print(1)
    else:
        print(0)