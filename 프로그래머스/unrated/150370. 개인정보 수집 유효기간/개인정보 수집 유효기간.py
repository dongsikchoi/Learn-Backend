
def is_valid_privacy(before, today,expire_month):
    before_year, before_month, before_day = map(int,before.split('.'))
    today_year, today_month, today_day = map(int,today.split('.'))

    before_num_day = 28 * 12 *  before_year + 28 * (before_month - 1) + before_day 
    
    expire_day = before_num_day + expire_month * 28 
    today_num_day = 28 * 12 * today_year + 28 * (today_month - 1) + today_day
    
    if today_num_day >= expire_day:
        return False 
    else:
        return True 
def solution(today, terms, privacies):
    answer = []
    terms_hash = dict() 
    for term in terms:
        privacy, expire_month = term.split(' ')
        terms_hash[privacy] = int(expire_month)
    print(terms_hash)
    count = 0
    for privacy in privacies: 
        count += 1
        before, term = privacy.split(' ')
        is_valid = is_valid_privacy(before, today, terms_hash[term])
        if not is_valid:
            answer.append(count)
        
    
    return answer