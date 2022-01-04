import sys
n=int(sys.stdin.readline())
dp=[0]*(n+1)
dp[1]=1
number=[]
for i in range(int(n**0.5)+1):
    number.append(i**2)

for j in range(1,len(number)):
    if number[i]<n:
        dp[i]