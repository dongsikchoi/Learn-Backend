import sys 


word = sys.stdin.readline().strip()

result_list = [] 
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        tmp = word[0:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        result_list.append(tmp)
print(min(result_list))