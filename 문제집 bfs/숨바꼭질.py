import sys
from collections import deque
input = sys.stdin.readline

start,end = map(int,input().strip().split())

visit  = [-1]*100001
visit[start] = 0 
queue = deque()
queue.append(start)
def bfs():
    while queue:
        a = queue.popleft()
        for i in (a+1,a-1,a*2):
            if 0<=i<len(visit) and visit[i] == -1:
                visit[i] = visit[a] + 1
                queue.append(i)
        

bfs()
print(visit[end])

