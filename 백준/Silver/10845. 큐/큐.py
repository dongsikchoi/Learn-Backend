import sys
from collections import deque

num = int(sys.stdin.readline())
queue = deque()
for _ in range(num):
    command = sys.stdin.readline().strip()
    
    if 'push' in command:
        tmp_num = int(command.split(' ')[1])
        queue.append(tmp_num)

    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'pop':
        if queue:
            tmp_pop = queue.popleft()
            print(tmp_pop)
        else:
            print(-1)
        
    
