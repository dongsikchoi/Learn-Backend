import sys 

num = int(sys.stdin.readline())

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)


if num:
    score_list = []
    for _ in range(num):
        tmp_score =  int(sys.stdin.readline())
        score_list.append(tmp_score)
    score_list.sort()
    rm_num = my_round(num * 0.15)
    if rm_num > 0:
        final_score_list = score_list[rm_num: -rm_num]
        print( my_round(sum(final_score_list if rm_num else final_score_list) / (num - rm_num * 2)) )
    else:
        print( my_round(sum(score_list) / num))
else:
    print(0)