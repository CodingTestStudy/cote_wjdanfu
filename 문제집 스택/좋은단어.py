import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

result = 0
for i in range(n):
    my_str = input().strip()
    stack=deque()
    for i in my_str:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) ==0:
        result +=1
print(result)

