def solution(board, moves):
    stack = []
    answer = 0
    k = 0

    for i in moves:
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                k -= 2

        for j in range(len(board)):

            if board[j][i - 1] > 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                k += 1
                break

    return answer
