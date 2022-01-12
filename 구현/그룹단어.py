import sys

input = sys.stdin.readline

n = int(input())
count=0
for i in range(n):
    my_str = input().strip()
    flag = True
    for j in range(len(my_str)-1):
        temp = my_str[j]
        if my_str[j+1] == temp:
            continue
        else:
            for k in range(j+1,len(my_str)):
                if my_str[k] == temp:
                    flag = False
    if flag:
        count+=1
print(count)