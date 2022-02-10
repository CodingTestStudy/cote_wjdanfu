import sys
from collections import deque
high, start, end ,up ,down = map(int, input().split())

dx = [up,-down]

visit = [-1] * (high+1)

queue = deque()
queue.append(start)
visit[start] = 0 
def bfs():
    while queue:
        a= queue.popleft()
        for i in range(2):
            x = a + dx[i]
            if 0<x<=high and visit[x] == -1:
                visit[x] = visit[a] + 1
                queue.append(x)

bfs()

if visit[end] == -1:
    print("use the stairs")
else:
    print(visit[end])

