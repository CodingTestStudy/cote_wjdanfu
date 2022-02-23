import sys
from collections import deque

input = sys.stdin.readline

while True:
    floor, n,m = map(int,input().split())
    if floor == 0 and n ==0 and m ==0:
        break
    graph=[]
    for i in range(floor):
        k = []
        for j in range(n):
            k.append(list(input().strip()))
        graph.append(k)
        input()
    visit=[[[-1] * m for i in range(n)] for j in range(floor)]
    dx=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dz=[0,0,0,0,1,-1]
    queue = deque([])
    for i in range(floor):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] =='S':
                    visit[i][j][k] = 1
                    queue.append([i,j,k])
                    break
    result = 0
    flag =False
    while queue:
        a,b,c = queue.popleft()
        for i in range(6):
            x= a+dx[i]
            y= b+dy[i]
            z= c+dz[i]
            if 0<=x<floor and 0<=y<n and 0<=z<m and visit[x][y][z]==-1:
                if graph[x][y][z] == '.':
                    visit[x][y][z] = visit[a][b][c] + 1
                    queue.append([x,y,z])
                if graph[x][y][z] == 'E':
                    result = visit[a][b][c] +1
                    flag = True
                    break
    if flag:
        print("Escaped in {0} minute(s).".format(result))
    else:
        print("Trapped!")

