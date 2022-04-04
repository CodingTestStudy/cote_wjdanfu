import sys

input = sys.stdin.readline

n = int(input())

podo =[]
for i in range(n):
    podo.append(int(input()))

dp = [0] * (n+1)
if n == 1:
    print(podo[0])
    exit(0)
elif n == 2:
    print(podo[0]+podo[1])
    exit(0)
elif n == 3:
    print(max(podo[0]+podo[1],podo[1]+podo[2],podo[0]+podo[2]))
    exit(0)
dp[0] = podo[0]
dp[1] = podo[0]+podo[1]
dp[2] = max(podo[0]+podo[1],podo[1]+podo[2],podo[0]+podo[2])

for i in range(3,len(podo)):
    dp[i] = max(podo[i]+podo[i-1]+dp[i-3],podo[i]+dp[i-2])

print(max(dp))
