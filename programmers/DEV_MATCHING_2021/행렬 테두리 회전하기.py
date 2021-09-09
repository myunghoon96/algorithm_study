#https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    matrix = [[0]*columns for _ in range(rows)]
    for row in range(rows):
        for col in range(columns):
            matrix[row][col] = row*columns + col+1
    
    for query in queries:


        x1,y1,x2,y2 = query
        x1,y1,x2,y2 = x1-1, y1-1, x2-1, y2-1
        xy=[]
        val=[]
        # print(x1,y1,x2,y2)
        for col in range(y1,y2):
            xy.append((x1,col))

        for row in range(x1,x2+1):
            xy.append((row,y2))

        temp=[]
        for col in range(y1,y2):
            temp.append((x2,col))
        temp.reverse()
        xy+=temp

        temp=[]
        for row in range(x1+1,x2):
            temp.append((row,y1))
        temp.reverse()
        xy+=temp

        for row, col in xy:
            val.append(matrix[row][col])

        answer.append(min(val))
        for i, (x,y) in enumerate(xy):
            # if i==0:
            #     matrix[x][y]=val[-1]
            #     # print(x,y,val[-1])
            #     continue

            matrix[x][y]=val[i-1]

    
    return answer