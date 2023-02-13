def solution(babbling):

    word_list = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for baby in babbling:
        for word in word_list:
            baby = baby.replace(word,',',1)
        if baby.replace(',','') == '':
            answer += 1
    return answer