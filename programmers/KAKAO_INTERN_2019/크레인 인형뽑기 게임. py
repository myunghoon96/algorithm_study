#https://programmers.co.kr/learn/courses/30/lessons/64061

from collections import deque
def solution(board, moves):
    answer = 0

    board_size = len(board)
    new_board = [deque() for _ in range(board_size)]

    for row in range(board_size):
        for col in range(board_size):
            if board[row][col]!=0:
                new_board[col].append(board[row][col])
                
    stack = []
    for move in moves:
        move -= 1 # index
        if len(new_board[move])>0:
            pop_element = new_board[move].popleft()
            if len(stack)>0 and stack[-1] == pop_element:
                stack.pop()
                answer+=2
                continue
            stack.append(pop_element)
        
    return answer