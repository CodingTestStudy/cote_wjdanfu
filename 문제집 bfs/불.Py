import sys
from collections import deque

input = sys.stdin.readline

dx= [-1,1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(input().strip()))
fire = [[10000000]*m for i in range(n)]
me = [[-1]*m for i in range(n)]


queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] =='F':
            fire[i][j] = 0
            queue.append([i,j])
            break

while queue:
    a,b=queue.popleft()
    for i in range(4):
        x=a+dx[i]
        y=b+dy[i]
        if 0<=x<n and 0<=y<m and fire[x][y] == 10000000:
            if graph[x][y] != '#':
                fire[x][y] = fire[a][b] + 1
                queue.append([x,y])

for i in range(n):
    for j in range(m):
        if graph[i][j] =='J':
            me[i][j] = 0
            queue.append([i,j])
            break
flag = True
while queue:
    a,b = queue.popleft()
    for i in range(4):
        x= a+dx[i]
        y= b+dy[i]
        if not (0<=x<n and 0<=y<m):
            print(me[a][b]+1)
            flag=False
            exit(0)
        else:
            if me[x][y] == -1:
                if graph[x][y] == '.' and fire[x][y]> me[a][b] +1:
                    me[x][y] = me[a][b]+1
                    queue.append([x,y])

if flag:
    print("IMPOSSIBLE")