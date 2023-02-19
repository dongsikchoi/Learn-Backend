import sys 

num = int(sys.stdin.readline())
bong_list = list(map(int,sys.stdin.readline().split()))


result_list = []
max_bong = 0 
count = 0 
for bong in bong_list:
    if bong > max_bong:
        max_bong = bong
        count = 0 
    else:
        count += 1 
    result_list.append(count)
print(max(result_list))
