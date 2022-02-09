import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

a,b=map(int,input().split())

M= int(input())
graph=[[] for i in range(N+1)]
visit = [0 for i in range(N+1)]

queue = deque()

for i in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

queue.append(graph[a])
visit[a]=1
count = 1
def bfs():
    global count
    while queue:
        temp = []
        k = queue.popleft()
        for i in k:
            visit[i]=1
            if i == b:
                print(count)
                exit(0)
            else:
                for j in graph[i]:
                    if visit[j]==0:
                        temp.append(j)
        if len(temp)>0:
            queue.append(temp)
            count+=1

bfs()
if visit[b] == 0:
    print(-1)