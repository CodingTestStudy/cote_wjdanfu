a = int(input())

score=list(map(int,input().split()))

maxNum=max(score)
avg=0
for i in range(a):
  score[i]/=maxNum/100
  avg+=score[i]

print(avg/a)
