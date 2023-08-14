import sys

input = sys.stdin.readline
n = int(input())

limit = 41

d_zero = [0] * limit 
d_one = [0] * limit

d_zero[0], d_one[0] = 1,0 
d_zero[1], d_one[1] = 0,1 

for _ in range(n): 
    tmp_n = int(input())

    for i in range(2, tmp_n + 1):
        d_zero[i] = d_zero[i-1] + d_zero[i-2]
        d_one[i] = d_one[i-1] + d_one[i-2]
    print(f'{d_zero[tmp_n]} {d_one[tmp_n]}')