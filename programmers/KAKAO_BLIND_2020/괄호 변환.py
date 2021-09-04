#https://programmers.co.kr/learn/courses/30/lessons/60058#

def separate(a):
    l,r = 0,0
    
    for i in range(len(a)):
        if a[i]=='(':
            l+=1
        else:
            r+=1
        if l==r:
            return a[:i+1], a[i+1:]

def check_correct(a):
    stack=[]
    for i in range(len(a)):
        if a[i]=='(':
            stack.append(a[i])
        else:
            if len(stack)==0:
                return False
            stack.pop()
    
    if len(stack)==0:
        return True
    else:
        return False

def solution(p):

    #1
    if len(p)==0:
        return ''
    #2
    u,v = separate(p)
    #3
    if check_correct(u) == True:
        return u+solution(v)
    #4
    elif check_correct(u) == False:
        result='('
        result+=solution(v)
        result+=')'
        u=u[1:-1]

        for i in range(len(u)):
            if u[i]=='(':
                result+=')'
            else:
                result+='('
        return result  