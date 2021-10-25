#https://www.acmicpc.net/problem/17140

import sys
from collections import Counter
R,C,K = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

row, col = len(mat), len(mat[0])


time = 0
while True:
    if time > 100:
        print("TIME END")
        print(-1)
        break
    if R-1 <row and C-1<col and mat[R-1][C-1]==K:
        print("ANSWER")
        print(time)
        break
    print("TIME ", time)
    if row>=col:
        print("ROW FUNCTION START")
        new_mat = []
        max_row_length = -1
        for e in mat:
            temp = list(Counter(e).items())
            temp.sort(key = lambda x:(x[1],x[0]))
            temp_list=[]
            for key,v in temp:
                temp_list.append(key)
                temp_list.append(v)
            if len(temp_list)>100:
                temp_list=temp_list[:100]
            new_mat.append(temp_list)
            max_row_length = max(max_row_length, len(temp_list))

        for i,e in enumerate(new_mat):
            need = max_row_length - len(e)
            new_mat[i]+=[0]*need

        
        mat = new_mat
        row, col = len(mat), len(mat[0])
        print("row col", row, col)
        print("ROW FUNCTION END")

    else:
        print("COL FUNCTION START")
        trans_mat = list(map(list, zip(*mat)))
        
        new_mat = []
        max_col_length = -1
        for e in trans_mat:
            temp = list(Counter(e).items())
            temp.sort(key = lambda x:(x[1],x[0]))
            temp_list=[]
            for key,v in temp:
                if key == 0 :
                    continue
                temp_list.append(key)
                temp_list.append(v)
            if len(temp_list)>100:
                temp_list=temp_list[:100]
            new_mat.append(temp_list)
            max_col_length = max(max_col_length, len(temp_list))

        for i,e in enumerate(new_mat):
            need = max_col_length - len(e)
            new_mat[i]+=[0]*need

        

        new_result_mat = list(map(list, zip(*new_mat)))
        
        mat = new_result_mat
        row, col = len(mat), len(mat[0])
        print("row col", row, col)
        print("COL FUNCTION END")
        
    time+=1
