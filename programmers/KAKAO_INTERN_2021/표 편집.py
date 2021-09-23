#https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    answer = ''
    ans_list=[True for _ in range(n)]
    link_list = dict()
    link_list[0]=[n-1,1]
    link_list[n-1]=[n-2,0]
    for i in range(1,n-1):
        link_list[i]=[i-1,i+1]
    
    cur = k
    del_stack = []
    
    for c in cmd:
        split_list = c.split(' ')
        if len(split_list) == 2:
            ins, num = split_list
            
            if ins == 'U':
                for _ in range(int(num)):
                    cur = link_list[cur][0]

            elif ins == 'D':
                for _ in range(int(num)):
                    cur = link_list[cur][1]

        else:
            ins = split_list[0]
            if ins == 'C':
                ans_list[cur]=False
                pre_node, next_node = link_list[cur]
                link_list[pre_node][1]=next_node
                link_list[next_node][0]=pre_node
                del_stack.append((cur,pre_node,next_node))
                if next_node==0:
                    cur = pre_node
                elif next_node!=0:
                    cur = next_node
            elif ins == 'Z':
                r_node, r_pre, r_next = del_stack.pop()
                ans_list[r_node]=True
                link_list[r_pre][1]=r_node
                link_list[r_node]=[r_pre, r_next]
                link_list[r_next][0]=r_node

    # print(ans_list)
    for e in ans_list:
        if e==True:
            answer+='O'
        else:
            answer+='X'
    return answer