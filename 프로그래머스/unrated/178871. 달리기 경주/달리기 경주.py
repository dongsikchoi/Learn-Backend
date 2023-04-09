def solution(players, callings):
    hash = {call : index for index, call in enumerate(players)}
    for call in callings:
        tmp_index = hash[call]
        players[tmp_index - 1], players[tmp_index] = players[tmp_index], players[tmp_index - 1]
        hash[players[tmp_index]] = tmp_index 
        hash[players[tmp_index - 1]] = tmp_index - 1 
    return players