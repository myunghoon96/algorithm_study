#https://programmers.co.kr/learn/courses/30/lessons/60059


def rotate90(arr):
    row=len(arr)
    col=len(arr[0])
    result=[[0]*col for _ in range(row)]

    for r in range(row):
        for c in range(col):
            result[c][row-r-1]=arr[r][c]
            
    return result

def insertKey(startR,startC, key, keySize, lockSize, matrix_in):    
    matrixSize=keySize*2+lockSize
    matrix=[[0]*matrixSize for _ in range(matrixSize)]

    #copy matrix
    for i in range(keySize, keySize+lockSize):
        for j in range(keySize, keySize+lockSize):
            matrix[i][j]=matrix_in[i][j]

    #plus key value to matrix
    r=0
    for i in range(startR, startR + keySize):
        c=0
        for j in range(startC, startC + keySize):
            matrix[i][j]+=key[r][c]
            c+=1
        r+=1

    #check success
    for i in range(keySize, keySize+lockSize):
        for j in range(keySize, keySize+lockSize):
            if matrix[i][j]!=1:
                return False  
            
    return True



def solution(key, lock):
    keySize=len(key)
    lockSize=len(lock)
    
    key2=rotate90(key)
    key3=rotate90(key2)
    key4=rotate90(key3)
    kl=[key,key2,key3,key4]
    
    matrixSize=keySize*2+lockSize
    matrix=[[0]*matrixSize for _ in range(matrixSize)]
    r=0
    for i in range(keySize, keySize+lockSize):
        c=0 
        for j in range(keySize, keySize+lockSize):
            matrix[i][j]=lock[r][c]
            c+=1
        r+=1
        
    for r in range(matrixSize-keySize+1):
        for c in range(matrixSize-keySize+1):
            for key in kl:
                if insertKey(r, c, key, keySize, lockSize, matrix) == True:
                    return True

    return False