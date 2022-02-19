import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().strip().split())

r,c,d = map(int,input().strip().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().strip().split())))

queue = deque([])
queue.append([r,c,d])
count = 0
def bfs():
    global count
    while queue:
        a,b, d = queue.popleft()
        if graph[a][b] == 0:
            graph[a][b] = 2
            count += 1
        for _ in range(4):
            flag = False
            if d == 0:
                x = a
                y = b - 1
                d = 3
            elif d== 3:
                x = a + 1
                y = b
                d = 2
            elif d==2:
                x= a
                y = b+ 1
                d=1
            elif d ==1:
                x= a - 1
                y = b 
                d = 0
            if graph[x][y] == 0:
                queue.append([x,y,d])
                flag = True
                break
        if not flag:
            if d ==0:
                a += 1
                if graph[a][b] == 1:
                    break
                else:
                    queue.append([a,b,d])
            elif d == 1:
                b -= 1
                if graph[a][b] == 1:
                    break
                else:
                    queue.append([a,b,d])
            elif d ==2:
                a -= 1
                if graph[a][b] == 1:
                    break
                else:
                    queue.append([a,b,d])
            elif d ==3:
                b += 1
                if graph[a][b] == 1:
                    break
                else:
                    queue.append([a,b,d])
      
            
    return count
print(bfs())

