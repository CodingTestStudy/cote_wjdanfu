N, K = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid

    if total >= K:
        result = mid
        start = mid + 1
    elif total < K:
        end = mid - 1

print(result)
