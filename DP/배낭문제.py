import sys

input= sys.stdin.readline
N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else: # 최대 weight에서 지금 weigh를 뺀것의 가치랑 지금 weigh의 가치의 합과 그냥 있는거중 큰것
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j]) 

print(knapsack[N][K])