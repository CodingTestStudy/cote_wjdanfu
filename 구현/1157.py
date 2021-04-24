N=input().upper() # zZa
D=list(set(N))    #za
C=[] #[2,1]
for i in D:
   C.append(N.count(i))

if C.count(max(C)) > 1:
  print("?")
else:
  print(D[C.index(max(C))])
