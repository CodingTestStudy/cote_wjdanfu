n = int(input())

array = list(map(int, input().split()))

d= [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 2]+ array[i], d[i -1])

print(d[n])

'''
ex)
9 1 2 4 5 2 4 8 6

d
9 9 11 13 16 16 20 24 26
'''
