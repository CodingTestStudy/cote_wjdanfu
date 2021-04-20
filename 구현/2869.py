A,B,V=map(int,input().split())

if int((V-B)%(A-B))==0:
  print(int((V-B)/(A-B)))
else:
  print(int((V-B)/(A-B))+1)
