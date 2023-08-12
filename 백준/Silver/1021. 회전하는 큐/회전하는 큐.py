import sys
from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())

queue = deque([i for i in range(1, N+1)])
t_index_list = list(map(int, input().split()))

count = 0
for index in t_index_list:
    while True:
        if queue[0] == index:
            queue.popleft()
            break

        else:
            if queue.index(index) > len(queue)//2:
                queue.rotate(1)
                count += 1
            else:
                queue.rotate(-1)
                count += 1
print(count)