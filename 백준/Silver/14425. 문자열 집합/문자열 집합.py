import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input() for _ in range(N)])

count = 0
for _ in range(M):
    tmp_str = input()
    if tmp_str in S:
        count += 1
print(count)