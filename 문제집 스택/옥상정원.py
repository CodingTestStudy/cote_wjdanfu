import sys

input = sys.stdin.readline

n = int(input())

loof = []

for i in range(n):
    loof.append(int(input()))

loof = loof[::-1]


result = []

temp = []
temp.append([loof[0], 0])

for i in range(1, n):
    count = 0
    while temp and loof[i] > temp[-1][0]:
        count += temp[-1][1]
        temp.pop()
        count += 1
    temp.append([loof[i], count])
    result.append([loof[i], count])

k = 0
for i in result:
    k += i[1]
print(k)
