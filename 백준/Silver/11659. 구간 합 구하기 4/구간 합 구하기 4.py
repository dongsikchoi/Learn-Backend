import sys

input = sys.stdin.readline
N, M = map(int, input().split())

num_list = list(map(int, input().split()))
for i in range(N - 1):
    num_list[i+1] += num_list[i]
num_list = [0] + num_list


for _ in range(M):
    from_, to_ = map(int, input().split())
    print(num_list[to_] - num_list[from_-1])