while True:
  try:
    A = list(map(int,input().split()))
    K=0
    if A[1]-A[0]>A[2]-A[1]:
      K=A[1]-A[0]
    else:
      K=A[2]-A[1]

    print(K-1)
  except:
        break
