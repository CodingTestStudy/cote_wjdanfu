import sys
test=int(sys.stdin.readline())
for k in range(test):
    dic={}
    a=int(sys.stdin.readline())
    for i in range(a):
        m,n=sys.stdin.readline().strip().split()
        if n not in dic:
            dic[n]=1
        else:
            dic[n]+=1

    anwer=1
    for value in dic.values():
        anwer*=(value+1)

    print(anwer-1)