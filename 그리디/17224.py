N,L,K=map(int,input().split())

problem=[]

for i in range(N):
  problem.append(list(map(int,input().split())))

problem.sort(key=lambda x:x[1])
print(problem)

score=0
for i in range(K):
  if problem[i][1]<=L:
    score+=140
    continue
  elif problem[i][0]<=L:
    score+=100

print(score)
