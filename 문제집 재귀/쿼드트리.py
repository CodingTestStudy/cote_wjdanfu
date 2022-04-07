import sys

input = sys.stdin.readline

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int,input().strip())))


def solve(n,x,y):
    temp = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != temp:
                print('(',end="")
                solve(n//2,x,y)
                solve(n//2,x,y+n//2)
                solve(n//2,x+n//2,y)
                solve(n//2,x+n//2,y+n//2)
                print(')',end="")
                return
    if temp == 1:
        print(1,end="")
    if temp == 0:
        print(0,end="")

solve(N,0,0)