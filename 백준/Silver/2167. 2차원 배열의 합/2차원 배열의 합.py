import sys 

n, m = map(int, sys.stdin.readline().split())
overall_list = []

for _ in range(n): 
    tmp_list = list(map(int,sys.stdin.readline().split()))
    overall_list.append(tmp_list)

num = int(sys.stdin.readline())

for _ in range(num):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    tmp_result = 0
    for x_ in range(x1-1,x2):
        tmp_result += sum(overall_list[x_][y1 -1:y2])
    print(tmp_result)