base_list = [[0]*101 for _ in range(101)]
num = int(input())

for _ in range(num):
    x,y = list(map(int,input().split()))
    
    for x_ in range(x, x+10):
        for y_ in range(y, y+10):
            base_list[x_][y_] = 1
result = 0
for data in base_list:
    result += data.count(1)
print(result)