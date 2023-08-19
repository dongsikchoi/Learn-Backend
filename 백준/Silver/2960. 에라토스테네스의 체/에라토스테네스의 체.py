import sys

input = sys.stdin.readline

N, K = map(int, input().split())
target_list = [False] * (N + 1)
count = 0
for i in range(2, N + 1):
    if not target_list[i]:
        for j in range(i, N + 1, i):
            if not target_list[j]:
                target_list[j] = True
                count += 1
                if count == K:
                    print(j)