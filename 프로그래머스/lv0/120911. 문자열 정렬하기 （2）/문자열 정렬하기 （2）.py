def solution(my_string):
    answer=''.join(sorted(my_string,key=str.lower)).lower()
    return answer