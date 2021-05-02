n=int(input())
fir =1
last=n
while True:
  mid=(fir+last)//2
  if mid**2==n:
    print(mid)
    break
  elif mid**2>n:
    last=mid-1
  else:
    fir=mid+1
