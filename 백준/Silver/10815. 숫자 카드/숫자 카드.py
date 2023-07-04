sk_num = int(input())
sk_list = list(map(int,input().split()))
sk_dict = dict() 
for sk in sk_list:
    sk_dict[sk] = 0
can_num = int(input())
can_list = list(map(int,input().split()))

for can in can_list:
    try:
        is_in = sk_dict[can]
        print(1,end=' ')
    except:
        print(0,end=' ')