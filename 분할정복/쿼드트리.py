import sys
a=int(sys.stdin.readline())
graph=[]
for i in range(a):
    graph.append(list(map(int,sys.stdin.readline().strip())))

def solve(a,x,y):
    k=graph[x][y]
    for i in range(a):
        for j in range(a):
            if graph[x+i][y+j]!=k:
                print('(',end="")
                solve(a//2,x,y)
                solve(a//2,x,y+a//2)
                solve(a//2,x+a//2,y)
                solve(a//2,x+a//2,y+a//2)
                print(')',end="")
                return
            
    print(k,end="")
solve(a,0,0)