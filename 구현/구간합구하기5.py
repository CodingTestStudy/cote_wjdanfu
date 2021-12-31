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

for i in range(M):
    x1,y1,x2,y2=(map(int,input().split()))
    temp=0
    for j in range(x1-1,x2):
        temp+=dp[j][y2]-dp[j][y1-1]
    print(temp)


    