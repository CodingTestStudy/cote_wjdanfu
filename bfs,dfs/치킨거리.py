import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline

n,m= map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

house = deque([])
chicken=deque([])
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append([i,j])
        if graph[i][j]==2:
            chicken.append([i,j])

rrr=[]
for res in list(combinations(chicken, m)):
    result=0
    for k in house:
        my_min=10**6
        for j in range(len(res)):
            my_min=min(my_min,abs(res[j][0]-k[0])+abs(res[j][1]-k[1]))
        result+=my_min
    rrr.append(result)
        
print(min(rrr))