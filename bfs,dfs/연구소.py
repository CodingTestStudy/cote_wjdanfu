import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n,m=map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

emptys=deque([])
poisons=deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            emptys.append([i,j])
        if graph[i][j]==2:
            poisons.append([i,j])


walls=list(combinations(emptys, 3))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
rrr=[]
for wall in walls:
    count=0
    temp=copy.deepcopy(poisons)
    new_graph=copy.deepcopy(graph)
    for i in wall:
        new_graph[i[0]][i[1]]=1
    visited=[[-1] * m for _ in range(n)]
    while temp:
        x,y=temp.popleft()
        visited[x][y]=1
        for j in range(4):
            a=x+dx[j]
            b=y+dy[j]
            if 0<=a<n and 0<=b<m and new_graph[a][b]==0 and visited[a][b]==-1:
                new_graph[a][b]=2
                temp.append([a,b])
    for i in range(n):
        for j in range(m):
            if new_graph[i][j]==0:
                count+=1
    rrr.append(count)
print(max(rrr))