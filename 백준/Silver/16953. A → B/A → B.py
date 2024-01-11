import sys

num_a, num_b = map(int, sys.stdin.readline().split())
count = 1

while True:
    if num_a == num_b:
        print(count)
        break

    if num_b == 1:
        print(-1)
        break

    if str(num_b)[-1] == '1':
        num_b = int(str(num_b)[:-1])

    elif num_b % 2 == 0:
        num_b = num_b // 2

    else:
        print(-1)
        break
    count += 1
