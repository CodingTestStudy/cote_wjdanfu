import sys

from collections import defaultdict

n= int(input())

dic = defaultdict(str)

for i in range(n):
    name, state = map(str,input().split())
    dic[name] = state
for i in dic.values():
    print(i)