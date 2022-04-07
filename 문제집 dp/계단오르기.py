import sys

n = int(input())

dp = [0] * (n+1)

stair = [0]
for i in range(n):
    stair.append(int(input()))

dp[1] = stair[1]
if n == 1:
    print(dp[1])
    exit(0)

dp[2] = stair[1]+stair[2]
if n == 2:
    print(dp[2])
    exit(0)
dp[3] = max(stair[3]+stair[1],stair[2]+stair[3])

for i in range(4,n+1):
    dp[i] = max(stair[i]+dp[i-2],stair[i]+stair[i-1]+dp[i-3])
print(dp[n])
