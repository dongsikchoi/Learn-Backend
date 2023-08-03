import sys

input = sys.stdin.readline
n = int(input())
limit = 101
d = [0] * limit
d[1] = 1
d[2] = 1 
d[3] = 1

for _ in range(n):
    tmp_n = int(input())

    for i in range(4, tmp_n + 1):
        d[i] = d[i-2] + d[i-3]
    
    print(d[tmp_n])