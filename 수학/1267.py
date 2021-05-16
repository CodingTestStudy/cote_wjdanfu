a=int(input())

N=list(map(int,input().split()))

Y=10*a
M=15*a

for i in range(a):
  Y+=(N[i]//30)*10

for i in range(a):
  M+=(N[i]//60)*15

if Y==M:
  print("Y M",Y)
elif Y<M:
  print("Y",Y)
else:
  print("M",M)

