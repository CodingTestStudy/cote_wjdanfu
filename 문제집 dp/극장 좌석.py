import sys

input = sys.stdin.readline

def fibo(n):
    dp = [0] * (n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

n = int(input())
m = int(input())
vip=[]
for i in range(m):
    vip.append(int(input()))

arr=[]
answer = []
for i in range(1,n+1):
    k=1
    if not i in vip:
        arr.append(i)
    else:
        if len(arr)>2:
            k = fibo(len(arr))
        elif len(arr) ==1:
            k = 1
        elif len(arr) ==2:
            k = 2
        
        answer.append(k)
        arr=[]
k =1
if len(arr)>2:
    k = fibo(len(arr))
elif len(arr) ==1:
    k = 1
elif len(arr) ==2:
    k = 2    
answer.append(k)

result =1
for i in answer:
    result*=i
print(result)



