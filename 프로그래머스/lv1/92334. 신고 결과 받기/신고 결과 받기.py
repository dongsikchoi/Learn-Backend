def solution(id_list, report, k):
    answer = []
    answer_dict = {id : 0 for id in id_list}
    hash_=dict()
    for id in id_list:
        hash_[id] = [] 
        
    for report_ in report:
        from_, to_ = report_.split(' ')
        hash_[to_].append(from_)
    for report_target in hash_:
        report_from_list = list(set(hash_[report_target]))
        if len(report_from_list) >= k:
            for from_ in report_from_list:
                answer_dict[from_] += 1 
    
    for key,value in answer_dict.items():
        answer.append(value)
        
        
        
    
    return answer