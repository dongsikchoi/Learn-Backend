import sys

input = sys.stdin.readline
word = input()

result = ''
tmp_str = ''

for str_ in word:
    if str_ == '<' and tmp_str:
        tmp_str = tmp_str[::-1]
        result += tmp_str
        tmp_str = str_
    elif str_ == '>':
        tmp_str += '>'
        result += tmp_str
        tmp_str = ''
    elif str_ == ' ' and '<' not in tmp_str:
        tmp_str = tmp_str[::-1]
        result += tmp_str
        result += ' '
        tmp_str = ''
    else:
        tmp_str += str_
if tmp_str:
    tmp_str = tmp_str[::-1].strip()
    result += tmp_str
print(result)