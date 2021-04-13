a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))     # 스트링형태로 나눠서 result[]에 각각 넣어줌 
for i in range(10):
    print(result.count(str(i))) # 0에서 9까지 갯수 새서 각각 프린트함
    
###다른방법

a= int(input())
b= int(input())
c=int(input())
score=[0,0,0,0,0,0,0,0,0,0]

mul=str(a*b*c)
for i in range(mul.__len__()):
  k=int(mul[i])
  score[k] += 1

for i in range(score.__len__()):
  print(score[i])
