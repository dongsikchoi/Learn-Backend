import sys 

num = int(sys.stdin.readline())
meeting_list = []

for _ in range(num):
    from_, to_ = map(int, sys.stdin.readline().split())
    meeting_list.append([from_, to_])
    
meeting_list.sort(key=lambda x: (x[1], x[0]))

meeting_time = 0 
count = 0 

for meeting in meeting_list:
    if meeting_time <= meeting[0]:
        meeting_time = meeting[1]
        count += 1
print(count)