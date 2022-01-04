import sys

sys.stdin.readline

n,m,money = map(int,input().split())

fee = list(map(int,input().split()))

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    # 양방향 간선
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visit = [0]*n
def dfs(start):
    visit[start]=1
    global min_fee
    min_fee=min(fee[start],min_fee)
    for i in graph[start]:
        if visit[i]==0:
            dfs(i)
    return min_fee

result=0
z=0
for i in range(n):
    if visit[i]==0:
        min_fee=1000000000
        result=dfs(i)
        money-=result
        if money<0:
            print("Oh no")
            exit(0)
        z+=result


print(z)
