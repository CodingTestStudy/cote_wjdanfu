import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])
N,M = map(int,input().split())

graph=[]
visit = [[-1 for i in range(M)] for _ in range(N)]
for i in range(N):
    graph.append(list(input().strip()))
queue.append([0,0])

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs():
    while queue:
        x,y=queue.popleft()
        visit[x][y]=1
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<M and int(graph[a][b])==1:
                if visit[a][b]!=0:
                    graph[a][b] = int(graph[x][y])+1
                    queue.append([a,b])

bfs()
print(graph[N-1][M-1])


