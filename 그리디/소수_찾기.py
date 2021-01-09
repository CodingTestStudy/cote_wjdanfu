def solution(n):
    sosu = []
    if n!=2:
        for i in range(3, n+1):
            sosu.append(i)
            for j in range(2, i):
                if i%j == 0:
                    sosu.remove(i)
                    break
                
    if n == 2:
        return 1
    
    return len(sosu)+1

#정확도는 맞지만 시간복잡도가 O(n2) 이라 시간 초과가걸린다 2중 포문을 사용하지않고 짜보자
