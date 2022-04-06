import sys

input = sys.stdin.readline

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

print(graph)

one = 0 
zero = 0
def solve(n,x,y):
    global one
    global zero
    temp = graph[x][y]
    for i in range(x,n+x):
        for j in range(y,n+y):
            if graph[i][j] != temp:
                solve(n//2,x,y)
                solve(n//2,x+n//2,y)
                solve(n//2,x,y+n//2)
                solve(n//2,x+n//2,y+n//2)
                return
    if temp == 1:
        one+=1
    else: zero+=1



solve(N,0,0)
print(zero)
print(one)