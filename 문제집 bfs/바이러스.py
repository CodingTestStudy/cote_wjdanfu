import sys

input = sys.stdin.readline

N = int(input())

M = int(input())
graph = [[] for i in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0 for i in range(N+1)]
count=0
def dfs(start):
    global count
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == 0:
            count+=1
            dfs(i)

dfs(1)
print(count)

