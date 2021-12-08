def solve(k):
    num=1
    print('+')
    a=[]
    a.append(num)
    while True:
        if len(k)==0:
            break
        if len(a)==0:
            num+=1
            a.append(num)
        elif a[-1]!=k[-1]:
            num+=1
            a.append(num)
            print("+")
        else:
            k.pop()
            a.pop()
            print("-")



k=[1,2,5,3,4]
k.reverse()
solve(k)