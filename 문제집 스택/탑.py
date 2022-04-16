import sys

input = sys.stdin.readline

n = int(input())

top = list(map(int, input().split()))

result = [0] * n


temp = []
temp.append([top[0], 1])
for i in range(1, n):
    while temp and top[i] > temp[-1][0]:
        temp.pop()

    if temp and temp[-1][0] != top[i]:
        result[i] = temp[-1][1]

    temp.append([top[i], i+1])

for i in result:
    print(i, end=" ")
