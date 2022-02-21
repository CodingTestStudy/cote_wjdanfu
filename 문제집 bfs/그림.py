import sys
from collections import deque


input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
visit = [[-1]*m for i in range(n)] 
for i in range(n):
    graph.append(list(map(int,input().split())))


dx= [-1,1,0,0]
dy= [0,0,1,-1]

def bfs():
    count = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<n and 0<=y<m and visit[x][y] == -1:
                if graph[x][y]==1:
                    queue.append([x,y])
                    visit[x][y] = 1
                    count+=1
    return count
result=[]
num=0
for i in range(n):
    for j in range(m):
        if visit[i][j] == -1 and graph[i][j]==1:
            queue = deque([])
            queue.append([i,j])
            visit[i][j]=1
            result.append(bfs())
            num+=1

print(num)
if result:
    print(max(result))
else:
    print(0)