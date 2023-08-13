import sys

input = sys.stdin.readline

N = int(input())
distance_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))

min_price = price_list[0]
result = 0
for i in range(N - 1):
    if min_price > price_list[i]:
        min_price = price_list[i]
    result += min_price * distance_list[i]
print(result)