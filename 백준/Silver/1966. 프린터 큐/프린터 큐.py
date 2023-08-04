import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    N, M = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    index_queue = deque(list(range(N)))
    result = 0 

    while queue: 
        max_priority = max(queue) 
        if queue[0] != max_priority:
            queue.append(queue.popleft())
            index_queue.append(index_queue.popleft())
        else:
            queue.popleft()
            result += 1
            index = index_queue.popleft()
            if index == M:
                print(result)