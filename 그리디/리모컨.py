import sys

input=sys.stdin.readline

chnner=int(input())
ans = abs(100 - chnner)
num=int(input())


if num:
    broken=set(input().split())
else:
    broken=set()

for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        ans=min(ans,abs(chnner-i)+len(str(i)))
print(ans)