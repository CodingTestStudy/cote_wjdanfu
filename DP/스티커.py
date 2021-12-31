import sys

input=sys.stdin.readline

test=int(input())

for i in range(test):
    n= int(input())
    k=[]
    dp=[[0]*(n) for i in range(2)]
    for i in range(2):
        k.append(list(map(int,input().split())))
    dp[0][0]=k[0][0]
    dp[1][0]=k[1][0]
    for i in range(1,n):
        if i == 1:
            dp[0][i]=k[1][i-1]+k[0][i]
            dp[1][i]=k[0][i-1]+k[1][i]
        else:
            dp[0][i]=max(dp[1][i-2]+k[0][i],dp[1][i-1]+k[0][i])
            dp[1][i]=max(dp[0][i-2]+k[1][i],dp[0][i-1]+k[1][i])
    print(max(dp[0][-1],dp[1][-1]))