import sys 

a,b = sys.stdin.readline().split()
min_value = int(a.replace('6','5')) + int(b.replace('6','5'))
max_value = int(a.replace('5','6')) + int(b.replace('5','6'))
print(f'{min_value} {max_value}')