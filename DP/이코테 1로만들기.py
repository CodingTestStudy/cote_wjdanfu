n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

    if i % 5 == 0 and dp[i] > dp[i // 5] + 1:
        dp[i] = dp[i // 5] + 1


print(dp[n])

# dp 문제 유형을 파악하는게 중요 (완전 탐색으로 접근했을때 시간이 매우 오래걸릴때)
# 탑다운, 바텀업 유형에 맞게 바텀업이 더 좋음
