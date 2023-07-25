from typing import List 
size, index = map(int, input().split())
num_list = list(map(int,input().split()))

def merge_sort(num_list:List[int]) -> List[int]:
    size = len(num_list)
    if size == 1: 
        return num_list 

    mid = size // 2 

    left_num_list = num_list[:mid]
    right_num_list = num_list[mid:]

    sorted_left = merge_sort(left_num_list)
    sorted_right = merge_sort(right_num_list)
    
    sorted_num_list = [] 
    index_left = 0 
    index_right = 0 
    while index_left < len(sorted_left) or index_right < len(sorted_right): 
        if index_left == len(sorted_left): 
            sorted_num_list.append(sorted_right[index_right])
            index_right += 1 
            continue 
        if index_right == len(sorted_right):
            sorted_num_list.append(sorted_left[index_left])
            index_left += 1 
            continue 

        if sorted_right[index_right] <= sorted_left[index_left]: 
            sorted_num_list.append(sorted_right[index_right])
            index_right += 1 
        else: 
            sorted_num_list.append(sorted_left[index_left])
            index_left += 1 
    return sorted_num_list 

sorted_num_list = merge_sort(num_list)
print(sorted_num_list[index-1])