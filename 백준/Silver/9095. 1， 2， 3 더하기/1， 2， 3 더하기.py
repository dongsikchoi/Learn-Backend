import sys


n = int(sys.stdin.readline())
limit = 11 

d = [0] * limit
d[1] = 1 
d[2] = 2 
d[3] = 4 


for i in range(4,limit):
    d[i] = d[i-1] + d[i-2] + d[i-3]


for _ in range(n): 
    tmp_n = int(sys.stdin.readline())
    print(d[tmp_n])
