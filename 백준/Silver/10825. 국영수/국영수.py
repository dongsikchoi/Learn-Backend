import sys

input = sys.stdin.readline

N = int(input())
student_list = []

for _ in range(N):
    name, kor, eng, math = list(input().split())
    student_list.append([name, int(kor), int(eng), int(math)])

student_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in student_list:
    print(student[0])