# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''

    def split_uv(a):
        left, right = 0, 0
        for i in range(len(a)):
            if a[i] == '(':
                left += 1
            elif a[i] == ')':
                right += 1
            if left == right:
                return a[:i+1], a[i+1:]

        
    def check_correct(a):
        stack = []
        for i in range(len(a)):
            if a[i] == '(':
                stack.append('(')
            elif a[i] == ')':
                if len(stack) <= 0:
                    return False
                
                if stack and stack[-1] == '(':
                    stack.pop()
        
        if len(stack) != 0:
            return False
        
        return True
    
    def rev(a):
        result = ""
        for i in range(len(a)):
            if a[i] == '(':
                result += ')'
            else:
                result += '('
        return result
    
    def process(input_str):
        # 1
        if input_str == "":
            return ""
        # 2
        u, v = split_uv(input_str)
        # print(uv)
        # u, v = uv[0], uv[1]

        # 3
        if check_correct(u):
            return u + process(v)
        # 4
        if not check_correct(u):
            tmp_str = "("
            tmp_str += process(v)
            tmp_str += ")"
            tmp_str += rev(u[1:-1])
            return tmp_str
            
    answer = process(p)
    
    
    return answer