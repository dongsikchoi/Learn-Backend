import sys 

num = int(sys.stdin.readline())

for _ in range(num):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    tmp_list = list(range(1,n+1))
    
    
    for _ in range(k):
        tmp_value = 0 
        result_list = [] 
        for tmp in tmp_list: 
            tmp_value += tmp
            result_list.append(tmp_value)
        tmp_list = result_list
        
    print(result_list[-1])
    