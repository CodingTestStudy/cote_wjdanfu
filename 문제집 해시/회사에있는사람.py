import sys

from collections import defaultdict

n= int(input())

dic = defaultdict(str)

for i in range(n):
    name, state = map(str,input().split())
    dic[name] = state
s = sorted(dic.keys(), reverse=True)
for i in s:
    if dic[i]=='enter':
        print(i)