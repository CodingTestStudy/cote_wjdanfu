import sys
input= sys.stdin.readline

N,M=map(int,input().split())

m = [0]+list(map(int,input().split()))

c = [0]+list(map(int,input().split()))

dp = [[0]*(sum(c) + 1) for _ in range(N + 1)]
result=10**6
for i in range(1, N + 1):
    for j in range(1, sum(c) + 1):
        byte = m[i]
        cost = c[i]
       
        if j < cost:
            dp[i][j] = dp[i - 1][j] 
        else:
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j]) 

        if dp[i][j] >= M: 
            result = min(result, j)
print(result)