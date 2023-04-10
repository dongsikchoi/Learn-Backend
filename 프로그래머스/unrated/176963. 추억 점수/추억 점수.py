def solution(name, yearning, photo):
    hash = dict() 
    answer = []
    for i in range(len(name)):
        hash[name[i]] = yearning[i]
    for photo_ in photo: 
        tmp_answer = 0 
        for person in photo_:
            try:
                tmp_answer += hash[person]
            except:
                continue
        answer.append(tmp_answer)

    return answer