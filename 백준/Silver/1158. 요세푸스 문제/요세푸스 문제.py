import sys

n, k = map(int, sys.stdin.readline().split())

num_list = list(range(1, n + 1))
answer_list = []


current_idx = 0

while len(num_list) > 0:
    current_idx = (current_idx + k - 1) % len(num_list)
    answer_list.append(num_list.pop(current_idx))

answer = "<" + ", ".join(str(num) for num in answer_list) + ">"
print(answer)