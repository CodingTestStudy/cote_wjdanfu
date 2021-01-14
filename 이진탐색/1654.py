N, K = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))
start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if mid == 0:                   # mid가 0일때는 1로나눠서 될때밖에없다
            result = 1
            break
        elif i >= mid:
            total += i // mid

    if total >= K:
        result = mid
        start = mid + 1
    elif total < K:
        end = mid - 1

print(result)
