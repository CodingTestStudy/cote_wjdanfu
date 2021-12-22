import sys
from collections import deque
input=sys.stdin.readline
test=int(input())

for t in range(test):
    k=list(map(str,input().strip()))
    n=int(input())
    my_list=input().rstrip()[1:-1].split(',')
    queue=deque(my_list)
    flag=True
    count=0
   
    for i in k:
        if n==0 and i=='D':
            print('error')
            flag=False
            break
        if i=='R':
            count+=1
        if i=='D':
            if len(queue)==0:
                print('error')
                flag=False
                break
            else:
                if count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag:
        if count % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
        
        
