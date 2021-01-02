h=int(input());
sum=0;

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j)+ str(k):
        sum+=1;


print(sum);

# 파이썬 문자열 처리로하면 훨신간단하게 풀린다
