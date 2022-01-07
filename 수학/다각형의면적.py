import sys

input = sys.stdin.readline

n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


graph.append(graph[0])

fir=0
sec=0
for i in range(len(graph)-1):
    fir+=graph[i][0]*graph[i+1][1]
    sec+=graph[i][1]*graph[i+1][0]

result = (fir-sec)/2
print(abs(result))
