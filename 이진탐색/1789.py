s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)

# 이진탐색으로 풀이
s = int(input())
n = 1
answer = 0

start = 1
end = s
while start <= end:
    mid = (start + end) // 2

    if mid * (mid + 1) // 2 <= s:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
