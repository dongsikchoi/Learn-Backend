import sys

input = sys.stdin.readline
N, M= map(int,input().split())

index_dict = dict()
pokemon_dict = dict()

index = 1 
for _ in range(N):
    tmp_pokemon = input().strip() 
    index_dict[index] = tmp_pokemon
    pokemon_dict[tmp_pokemon] = index
    index += 1 

for _ in range(M): 
    q = input().strip() 
    if q.isdigit():
        print(index_dict[int(q)])
    else:
        print(pokemon_dict[q])