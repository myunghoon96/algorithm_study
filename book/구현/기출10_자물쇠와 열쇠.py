#https://programmers.co.kr/learn/courses/30/lessons/60059

import copy

def solution(key, lock):
    answer = True
    N = len(lock)
    M = len(key)
    
    def rotate(matrix):
        N = len(matrix)
        new_matrix = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_matrix[j][N-1-i] = matrix[i][j]
#         0,2 1,2. 2,2    =>   0,0 0,1 0,2.
        return new_matrix

    K = N+2*(M-1)
    new_lock = [[0]*K for _ in range(K)]
    for i in range(N):
        for j in range(N):
            new_lock[i+(M-1)][j+(M-1)] = lock[i][j]
            
    new_lock_90 = rotate(new_lock)
    new_lock_180 = rotate(new_lock_90)
    new_lock_270 = rotate(new_lock_180)

    def check_key_match(inserted_lock):
        for i in range(N):
            for j in range(N):
                if inserted_lock[i+(M-1)][j+(M-1)] != 1:
                    return False
        return True
    
    def insert_key(x, y):
        l1 = copy.deepcopy(new_lock)
        l2 = copy.deepcopy(new_lock_90)
        l3 = copy.deepcopy(new_lock_180)
        l4 = copy.deepcopy(new_lock_270)
        
        for i in range(M):
            for j in range(M):
                l1[x+i][y+j] += key[i][j]
                l2[x+i][y+j] += key[i][j]
                l3[x+i][y+j] += key[i][j]
                l4[x+i][y+j] += key[i][j]
        
        if check_key_match(l1) or check_key_match(l2) or check_key_match(l3) or check_key_match(l4):
            return True
        
        return False
        
    answer = False
    for i in range(K-(M-1)):
        for j in range(K-(M-1)):
            if insert_key(i,j):
                answer = True
    
    return answer