import sys

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

init_list = list(map(int,sys.stdin.readline().split()))
n = init_list[0]
k = init_list[1]
result = (factorial(n)) / ((factorial(k)) * (factorial(n - k)))
print(int(result))
