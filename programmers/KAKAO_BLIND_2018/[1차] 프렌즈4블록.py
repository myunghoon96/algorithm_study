#https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    row=m
    col=n
    matrix = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            matrix[i][j]=board[i][j]
        
    def check():
        l=[]
        for i in range(row-1):
            for j in range(col-1):
                if matrix[i][j]=='X':
                    continue
                    
                if matrix[i][j]==matrix[i][j+1] and matrix[i][j]==matrix[i+1][j] and matrix[i][j]==matrix[i+1][j+1]:
                    l.append((i,j))
                    l.append((i,j+1))
                    l.append((i+1,j))
                    l.append((i+1,j+1))
        return l
    
    def delete(dl):

        for x,y in dl:
            matrix[x][y]='X'

    
    def move():
        i=row

        for r in range(row):
            i-=1
            for j in range(col):
                if matrix[i][j]=='X':
                    continue
                mov=1
                flag=False

                while i+mov<row:
                    if matrix[i+mov][j] != 'X':
                        break
                    else:
                        flag=True                        
                        mov+=1

                
                if flag == True:
                    matrix[i+mov-1][j]=matrix[i][j]
                    matrix[i][j]='X'
            

    while True:
       
        dl = check()
        if len(dl)==0:
            break

        answer+=len(set(dl))
        delete(dl)
        move()

  
    return answer