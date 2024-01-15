import sys 

str_ = sys.stdin.readline()
count = 0 
for i in range(len(str_) - 1):
    if str_[i] != str_[i+1]:
        count += 1 
print(count//2)