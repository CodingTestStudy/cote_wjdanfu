N = int(input())

M, K = map(int, input().split())

pen = list(map(int, input().split()))
def solution():
    people = M * K

    pen.sort(reverse=True)
    result = 0
    for i in pen:
        people -= i
        result += 1
        if people <= 0:
            return result
            break
    stress = "STRESS"
    if people > 0:
        return stress

print(solution())
