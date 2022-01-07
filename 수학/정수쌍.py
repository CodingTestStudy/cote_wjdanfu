test=int(input())

for _ in range(test):
    count=0
    n,m=map(int,input().split())
    for i in range(1,n):
        for j in range(i+1,n):
            k=(i**2+j**2+m)/(i*j)
            if k.is_integer():
                count+=1
    print(count)