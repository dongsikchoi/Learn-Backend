import sys 

count = 1
while True:
    l,p,v = map(int,sys.stdin.readline().split())
    if v==0:
        break
    
    div = v // p 
    noco = v % p
    result = ( div * l ) + min(noco,l)
    print(f'Case {count}: {result}')
    count += 1