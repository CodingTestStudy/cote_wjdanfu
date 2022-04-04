import sys
from collections import deque

input = sys.stdin.readline

pipe = input().strip()

stack = deque()
my = 0

result = 0
for i in pipe:
    if len(stack)==0:
        my+=1
        stack.append(i)
        
    elif i == '(':
        my+=1
        stack.append(i)
    elif stack[-1] == '(' and i ==')':
        my -= 1
        result += my
        stack.append(i)
    elif stack[-1] == ')' and i==')':
        result+=1
        my -=1
        stack.append(i)
print(result)
