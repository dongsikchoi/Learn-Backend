import sys

input = sys.stdin.readline
num = int(input())
row = 1 

while num > row:
    num -= row
    row += 1 

if row % 2 == 0:
    numerator = num
    denominator = row - num + 1
else:
    numerator = row - num + 1
    denominator = num 

print(f'{numerator}/{denominator}')
