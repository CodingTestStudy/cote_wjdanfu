import sys
from collections import defaultdict

input = sys.stdin.readline

my_str = input().strip()

my_dic = defaultdict(int)

for i in range(len(my_str)):
    for j in range(len(my_str)-i):
        my_dic[my_str[j:j+i+1]] += 1

print(len(my_dic))
