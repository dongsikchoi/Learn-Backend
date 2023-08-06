import sys

input = sys.stdin.readline
n = int(input())
limit = 91

d = [0] * limit

d[1] = 1 
d[2] = 1 

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])