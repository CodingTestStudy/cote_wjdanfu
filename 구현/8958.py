n = int(input()) # 테스트 케이스 개수 입력 
score=[]
b=[]
for i in range(n): 
  score.append(input())

for i in range(n):
  result=0
  tmp=1
  for j in range(score[i].__len__()):
    if(score[i][j] == "O"):
      result += tmp
      tmp += 1
    else:
      tmp = 1
  print(result)
