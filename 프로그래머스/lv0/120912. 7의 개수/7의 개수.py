def solution(array):
    answer = 0
    str_ = ''
    for num in array: 
        str_ += str(num)
    answer = str_.count('7')
    return answer