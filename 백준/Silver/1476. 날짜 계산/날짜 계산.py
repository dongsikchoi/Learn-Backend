E, S, M = map(int, input().split())
e, s, m = 0, 0, 0 
result = 0 

while True:
    e += 1 
    s += 1
    m += 1 
    result += 1  

    if (E == e) and (S == s) and (M == m): 
        print(result)
        break 

    if e == 15: 
        e = 0 
    if s == 28:
        s = 0 
    if m == 19: 
        m = 0