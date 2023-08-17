import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    tmp_dict = dict()
    for _ in range(n):
        equip, part = input().split()
        if part in tmp_dict:
            tmp_dict[part].append(equip)
        else:
            tmp_dict[part] = [equip]
    result = 1
    for part in tmp_dict:
        result *= (len(tmp_dict[part]) + 1)
    print(result - 1)