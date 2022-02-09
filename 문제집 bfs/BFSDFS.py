from re import L
import sys
from collections import deque

input = sys.stdin.readline
N,M,start = map(int,input().split())

graph=[[] for _ in range(N+1)]
visit=[-1 for _ in range(N+1)]

for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()
queue = deque()

def dfs(start):
    print(start,end=" ")
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == -1:
            dfs(i)
def bfs():
    while queue:
        x=queue.popleft()
        if visit[x] == -1:
            print(x,end=" ")
            visit[x]=1
            for i in graph[x]:
                if visit[i] == -1:
                    queue.append(i)

dfs(start)
print()
visit=[-1 for _ in range(N+1)]
queue.append(start)
bfs()