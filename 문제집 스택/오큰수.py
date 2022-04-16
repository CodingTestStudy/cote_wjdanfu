from collections import deque
n = int(input())

k = list(map(int, input().split()))

arr = [-1] * n

queue = deque([])

queue.append([k[0], 0])
for i in range(1, n):
    while queue and queue[-1][0] < k[i]:
        arr[queue[-1][1]] = k[i]
        queue.pop()
    queue.append([k[i], i])
print(*arr)
