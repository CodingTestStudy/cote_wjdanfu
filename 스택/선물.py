import sys
from collections import deque
import heapq
input=sys.stdin.readline

n=int(input())
queue=[]
for i in range(n):
    santa=input().strip()
    if santa=='0':
        if len(queue)!=0:
            print(-heapq.heappop(queue))
        else:
            print(-1)
    else:
        gift=list(map(int,santa.split()))
        for i in range(1,len(gift)):
            heapq.heappush(queue,-gift[i])