# https://www.acmicpc.net/problem/1285

from copy import copy
import sys
import copy

N = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline()) for _ in range(N)]
#reverse whole matrix first, and use part of it
reverse_matrix = copy.deepcopy(matrix)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'H':
            reverse_matrix[i][j] = 'T'
        else:
            reverse_matrix[i][j] = 'H'  
answer = 20*20 + 1

#1<<N(= 2**N) cases for reversing rows
for bit in range(1<<N):
    # print('bit', bit)
    # copy_matrix = copy.deepcopy(matrix)
    copy_matrix = []
    #reverse specific rows
    for i in range(N):
        if bit & (1<<i):
            # print('i, 1<<i ',i, 1<<i)
            copy_matrix.append(reverse_matrix[i])
        else:
            copy_matrix.append(matrix[i])
            # for j in range(N):
            #     if copy_matrix[i][j] == 'H':
            #         copy_matrix[i][j] = 'T'
            #     else:
            #         copy_matrix[i][j] = 'H'  

    ttl_t = 0
    for col in range(N):
        cnt_t = 0
        for row in range(N):
            if copy_matrix[row][col] == 'T':
                cnt_t += 1
        
        #reverse col: cnt_t, NOT reverse col: N-cnt_t
        ttl_t += min(cnt_t, N-cnt_t)

    answer = min(answer, ttl_t)

print(answer)
