import sys

input = sys.stdin.readline
num_pc = int(input())
link = int(input())

graph = [[] for _ in range(num_pc + 1)]
visited = [0] * (num_pc + 1)

for _ in range(link): 
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(virus):
    visited[virus] = 1 

    for index in graph[virus]:
        if visited[index] == 0: 
            dfs(index)
dfs(1) 
print(sum(visited)-1)