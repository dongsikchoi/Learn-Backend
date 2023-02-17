n = int(input())

bees = 1 
count = 1 

while n > bees:
    bees += (6*count)
    count += 1 
print(count)