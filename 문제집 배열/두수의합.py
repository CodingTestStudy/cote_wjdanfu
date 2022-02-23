import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

x = int(input())

my_list = [0] * (1000001)
result = 0
for i in range(n):
    my_list[arr[i]] = 1
    if arr[i] != x-arr[i] and x-arr[i]>=0 and my_list[x-arr[i]] == 1:
        result +=1
print(result)
