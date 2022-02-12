import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int,input().split())
graph= []
for i in range(n):
    graph.append(list(map(int,input().split())))
graph2= [item[:] for item in graph]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
queue = deque([])
def bing(a,b):
    for i in range(4):
        x= a+dx[i]
        y= b+dy[i]
        if 0<=x<n and 0<=y<m and graph[x][y] == 0:
            if graph2[a][b] !=0:
                graph2[a][b]-=1

def bfs():
    while queue:
        a,b = queue.popleft()
        visit[a][b] = 1
        for i in range(4):
            x= a+dx[i]
            y= b+dy[i]
            if 0<=x<n and 0<=y<m and graph[x][y] != 0 and visit[x][y] == -1:
                visit[x][y] = 1
                queue.append([x,y])

result = 0
while True:
    count = 0
    visit = [[-1] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if graph2[i][j] != 0 and visit[i][j] == -1:
                queue.append([i,j])
                bfs()
                count +=1
                

    if count == 1:
        for i in range(n):
            for j in range(m):
                if graph2[i][j] !=0:
                    bing(i,j)
        graph= [item[:] for item in graph2]
        result +=1
    elif count ==0:
        print(0)
        break
    else:
        print(result)
        break


