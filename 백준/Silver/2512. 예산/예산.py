import sys 

num = int(sys.stdin.readline())
bud_list = list(map(int,sys.stdin.readline().split()))
overall_bud = int(sys.stdin.readline())

start, end = 0, max(bud_list)

while start <= end:
    midValue = (start + end) // 2 
    sum = 0 
    for budget in bud_list:
        if budget <= midValue:
            sum += budget 
        else:
            sum += midValue

    if sum <= overall_bud:
        start = midValue + 1 
    else:
        end = midValue - 1 
print(end)