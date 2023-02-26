import sys 

num = sys.stdin.readline().strip()
if len(num) == 1:
    origin_num = '0' + num
else:
    origin_num = num

count = 0 
while True:
    count += 1 
    if len(num) == 1:
        num = '0' + num
    tmp = str(int(num[0]) + int(num[1]))
    num = num[-1] + tmp[-1]
    if origin_num == num:
        print(count)
        break