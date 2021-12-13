import sys 
from collections import deque 

n=int(sys.stdin.readline())
graph=[]
possible=[]
shark=2
count=0
eat=0
queue=deque([])
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
        for j in range(n):
            if graph[i][j]==9:
                x,y=i,j
                graph[i][j]=0
while True:
    queue.append([x,y])
    for i in range(n):
        for j in range(n):
            if graph[i][j]!=0 and graph[i][j]<shark:
                possible.append([i,j,0])
                graph[i][j]=0
    if len(possible)==0:
        break
    visit=[[0]*n for _ in range(n)]
    while queue:
        visit[x][y]=0
        first,second=queue.popleft()
        for i in range(4):
            k=first+dx[i]
            l=second+dy[i]
            if k>=0 and l>=0 and k<n and l<n and visit[k][l]==0 and graph[k][l]<=shark:
                visit[k][l]= visit[first][second]+1
                queue.append([k,l])
    for i in range(len(possible)):
        if visit[possible[i][0]][possible[i][1]]==0:
            possible[i][2]=1000000
        else:
            possible[i][2]=visit[possible[i][0]][possible[i][1]]
    possible=sorted(possible, key=lambda x : x[1])
    possible=sorted(possible, key=lambda x : x[0])
    possible=sorted(possible, key=lambda x : x[2])
    if possible[0][2]==1000000:
        break
    x,y=possible[0][0],possible[0][1]
    count+=possible[0][2]
    eat+=1
    if eat>=shark:
        shark+=1
        eat=0

    possible.pop(0)
print(count)