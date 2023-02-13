import sys
num = int(sys.stdin.readline())
stack = []
for _ in range(num):
    command = sys.stdin.readline().strip()
    
    if 'push' in command:
        tmp_num = int(command.split(' ')[1])
        stack.append(tmp_num)

    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'pop':
        if stack:
            tmp_pop = stack.pop()
            print(tmp_pop)
        else:
            print(-1)