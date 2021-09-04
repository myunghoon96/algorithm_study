#https://programmers.co.kr/learn/courses/30/lessons/60061

def del_success(result,row_in,col_in,a_in):
    result.remove((col_in,row_in,a_in))
    
    for col,row,a in result:
        if a==0:
            if row==0 or (col-1,row,1) in result or (col,row,1) in result or (col,row-1,0) in result:
                continue
            else:
                # print("NOT DEL")
                result.add((col_in,row_in,a_in))
                return False
            
        elif a==1:
            if (col,row-1,0) in result or (col+1,row-1,0) in result or (col-1,row,1) in result and (col+1,row,1) in result:
                continue
            else:
                # print("NOT DEL")
                result.add((col_in,row_in,a_in))
                return False
    return True
                    

def solution(n, build_frame):
    result=set()
    answer = []

    for x,y,a,b in build_frame:
        row=y
        col=x
        
        #add
        if b==1:
            if a==0:
                if row==0 or (col-1,row,1) in result or (col,row,1) in result or (col,row-1,0) in result:
                    result.add((col,row,0))
                else:
                    # print("NOT ADD", x,y,a,b)
                    continue

            if a==1:
                if (col,row-1,0) in result or (col+1,row-1,0) in result or (col-1,row,1) in result and (col+1,row,1) in result:
                    result.add((col,row,1))
                else:
                    # print("NOT ADD", x,y,a,b)
                    continue
        #delete
        elif b==0:
            del_success(result,row,col,a)
            
            
    answer=list(result)    
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    
    return answer