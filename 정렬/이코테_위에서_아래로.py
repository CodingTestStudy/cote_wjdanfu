N = int(input())

array = []

for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)
print(array)

# array = sorted(array, reverse = True) 도 사용가능
