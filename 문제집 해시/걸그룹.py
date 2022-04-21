import sys
from collections import defaultdict

input = sys.stdin.readline

my_dic = defaultdict(list)

N, M = map(int, input().split())

for i in range(N):
    group = input().strip()
    member_num = int(input())
    for j in range(member_num):
        my_dic[group].append(input().strip())

for i in range(M):
    problem = input().strip()
    num = int(input())
    if num == 0:
        k = []
        for i in range(len(my_dic[problem])):
            k.append(my_dic[problem][i])
            k.sort()
        for _ in k:
            print(_)
    elif num == 1:
        for j in my_dic:
            if problem in my_dic[j]:
                print(j)
                break
