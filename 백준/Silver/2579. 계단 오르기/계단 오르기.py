import sys

input = sys.stdin.readline
n = int(input())
limit = 301

stair_list = [0] * limit
for i in range(1,n+1):
    stair_list[i] = int(input())

d=[0]*limit
d[1] = stair_list[1]
d[2] = stair_list[1] + stair_list[2]
d[3] = max(stair_list[2]+stair_list[3],stair_list[1]+stair_list[3])

for i in range(4, n+1): 
    d[i] = max(d[i-3] + stair_list[i-1] + stair_list[i], d[i-2] + stair_list[i])

print(d[n])