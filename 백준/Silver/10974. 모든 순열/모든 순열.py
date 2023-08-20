import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
num_list = permutations([i for i in range(1, N + 1)])

for set_ in num_list:
    print(*set_)