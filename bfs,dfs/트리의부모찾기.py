import sys

input=sys.stdin.readline

n= int(input())

graph=[[] for i in range(n+1)]
visit=[-1] * (n+1)
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    for i in graph[start]:
        if visit[i]==-1:
            visit[i]= start
            dfs(i)

dfs(1)
print(visit)
for i in range(2,n+1):
    print(visit[i])
