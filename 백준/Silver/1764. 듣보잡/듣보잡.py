import sys

input = sys.stdin.readline
N, M = map(int, input().split())

not_heard = dict()
result_dict = dict()

for _ in range(N):
    tmp_person = input()
    not_heard[tmp_person] = True

for _ in range(M):
    tmp_person = input()
    if tmp_person in not_heard:
        result_dict[tmp_person] = True

print(len(result_dict))
for key, value in sorted(result_dict.items()):
    print(key, end='')