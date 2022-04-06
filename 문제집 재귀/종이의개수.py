import sys

input = sys.stdin.readline


N = int(input())
graph=[]

for i in range(N):
    graph.append(list(map(int,input().split())))


one =0
minus = 0
zero = 0
def solve(n,x,y):
    global zero
    global one
    global minus
    temp = graph[x][y]
    for i in range(n):
        for j in range(n):
            if graph[i+x][j+y] != temp:
                solve(n//3,x,y)  # 0, 0
                solve(n//3,x+n//3,y) # 1, 0
                solve(n//3,x+(n//3*2),y) # 2, 0
                solve(n//3,x,y+n//3) #0 ,1
                solve(n//3,x+n//3,y+n//3)# 1,1
                solve(n//3,x+(n//3*2),y+(n//3*2))#2,2
                solve(n//3,x,y+(n//3*2))#0,2
                solve(n//3,x+n//3,y+(n//3*2))#1,2
                solve(n//3,x+(n//3*2),y+n//3) # 2,1
                return
    if temp == 0:
        zero+=1
    elif temp ==1:
        one+=1
    elif temp ==-1:
        minus+=1



solve(N,0,0)
print(minus)
print(zero)
print(one)
