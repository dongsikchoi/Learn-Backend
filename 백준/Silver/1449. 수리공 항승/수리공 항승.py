import sys 

input = sys.stdin.readline
N, L = map(int,input().split())
water_leak_loc = list(map(int,input().split()))

water_leak_loc.sort()
count = 1 

from_ = water_leak_loc[0] -1
end = from_ +  L 

for  i in range(1,N):
	if water_leak_loc[i] <= end:
		continue
	else:
		count += 1
		from_ = water_leak_loc[i] - 1
		end = from_ + L
print(count)