import sys
N=int(input())
result=1
for i in range(N):
  n = int(sys.stdin.readline()) # input으로 받으면 시간초과가난다
  result+=n

print(result-N)
