def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return "yes"
    return "no"


N = int(input())
array1 = list(map(int, input().split()))
array1.sort()

M = int(input())
array2 = list(map(int, input().split()))

for i in range(M):
    result = binary_search(array1, array2[i], 0, N)
    print(result, end=' ')
