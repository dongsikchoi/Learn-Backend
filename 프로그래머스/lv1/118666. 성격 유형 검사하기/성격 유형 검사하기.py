def solution(survey, choices):
    answer = ''
    index_dict = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    
    num = len(index_dict)  / 2
    for survey_, choices_ in zip(survey,choices):
        if choices_ > num:
            index_dict[survey_[1]] += choices_ - num
        elif choices_ < num :
            index_dict[survey_[0]] += num - choices_
    
    dict_items = list(index_dict.items())
    
    for i in range(0,len(index_dict),2):
        if dict_items[i + 1][1] > dict_items[i][1]:
            answer += dict_items[i+1][0]
        else:
            answer += dict_items[i][0]
    
    
    return answer