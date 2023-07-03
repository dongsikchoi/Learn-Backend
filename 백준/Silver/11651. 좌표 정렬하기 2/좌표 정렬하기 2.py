num = int(input())
result_list = []
for _ in range(num):
    tmp_x, tmp_y = map(int,input().split())
    result_list.append([tmp_y,tmp_x])
result_list.sort()
for y, x in result_list:
    print(x, y)