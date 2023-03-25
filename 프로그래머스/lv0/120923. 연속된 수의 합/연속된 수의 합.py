def solution(num, total):
    
    tmp_mid = total // num
    return [i for i in range(tmp_mid - (num-1) // 2, tmp_mid + (num+2) // 2)]