n=int(input())
fir=[]
sec=[]
for i in range(n):
  k=list(input().split(" "))
  fir=list(k[0])
  sec=list(k[1])
  fir.sort()
  sec.sort()
  if fir==sec:
    print(k[0],"&",k[1], "are anagrams.")
  else:
    print(k[0],"&",k[1], "are NOT anagrams.") 
