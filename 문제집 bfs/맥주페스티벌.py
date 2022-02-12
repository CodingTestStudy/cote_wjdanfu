import sys
from collections import deque

input= sys.stdin.readline
testcase = int(input().strip())

def check(): 
    q = deque([start]) 
    visited = set() 
    while q: 
        x, y = q.popleft() 
        if abs(x-dst[0]) + abs(y-dst[1]) <= 1000: 
            return True 
        for i in range(n): 
            if i not in visited: 
                nx, ny = cos[i] 
                if abs(x-nx) + abs(y-ny) <= 1000: 
                    q.append([nx, ny]) 
                    visited.add(i) 
    return False 


for _ in range(testcase):
    n = int(input().strip())
    

    start = [int(x) for x in input().strip().split()] 
    cos = [[int(x) for x in input().strip().split()] for _ in range(n)] 
    dst = [int(x) for x in input().strip().split()]

    if check(): 
        print("happy") 
    else: 
        print("sad")



    
            
            

