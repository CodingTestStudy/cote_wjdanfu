import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().strip())))
visit = [[0] * n for i in range(n)]
print(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue=deque([])
def bfs():
    k = 1
    while queue:
        a,b = queue.popleft()
        visit[a][b]=1
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<n and 0<=y<n and graph[x][y]==1 and visit[x][y] == 0:
                visit[x][y] = 1
                k+=1
                queue.append([x,y])
    return k

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j]==0:
            queue.append([i,j])
            result.append(bfs())
result.sort()
print(len(result))
for i in result:
    print(i)

