a=list(map(int,input().split()))

test = 0
for i in range(len(a)-1):
  if (a[i]-a[i+1])==1:
    test=1
  elif (a[i]-a[i+1]==-1):
    test=2
  else:
    test=3
    break

if test==2:
  print("ascending")
elif test==1:
  print("descending")
else:
  print("mixed")
