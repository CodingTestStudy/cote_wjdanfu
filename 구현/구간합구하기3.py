import sys

input=sys.stdin.readline

N,M=map(int,input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))

dp=[[0] for i in range(N)]
temp = 0    
for i in range(len(graph)):    # accumulate arr section 
    temp = 0    
    for j in range(len(graph)):
        temp +=graph[i][j]
        dp[i].append(temp)
print(dp)
for i in range(M):
    w=list(map(int,input().split()))
    if w[0] == 1:
        x1=w[1]
        y1=w[2]
        x2=w[3]
        y2=w[4]
        temp=0
        for j in range(x1-1,x2):
            temp+=dp[j][y2]-dp[j][y1-1]
        print(temp)
    if w[0] == 0:
        x1=w[1]
        y1=w[2]
        c=w[3]
        plus=c-graph[x1-1][y1-1]
        graph[x1-1][y1-1]=c
        for x in range(x1-1,x1):
            for y in range(y1,N+1):
                dp[x][y]+=plus
        print(dp)
        

    # 2 3 7 5
    # 0 2 5 12 17