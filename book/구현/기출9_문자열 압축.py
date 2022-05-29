# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = int(1e9)
    
    def compress(unit):
        nonlocal answer
        
        result = ""
        pre_e = s[0:unit]
        pre_cnt = 1
        last_remain = ""
        # print("pre_e", pre_e)
        for i in range(unit, len(s), unit):
            # print("s[i:i+unit]" ,s[i:i+unit])
            # if 0 < len(s[i:]) < unit:
            #     last_remain = s[i:]
            #     break
            if s[i:i+unit] == pre_e:
                pre_cnt += 1
            else:
                if pre_cnt == 1:
                    result += pre_e
                else:
                    result += (str(pre_cnt) + str(pre_e))
                pre_e = s[i:i+unit]
                pre_cnt = 1
        if pre_cnt == 1:
            result += pre_e
        else:
            result += (str(pre_cnt) + str(pre_e))
        # if last_remain != "":
        #     # print("ADD LAST REMAIN")
        #     result += last_remain
        # print(unit, result, len(result))
        answer = min(answer, len(result))
        return
    
    for compress_len in range(1, len(s)//2 +1):
    # for compress_len in range(1, len(s)):
        compress(compress_len)

    
    if len(s) == 1:
        return 1
    
    return answer


# def solution(s):
#     answer = 1001
#     size=1
    
#     if len(s)==1:
#         return 1
    
#     for size in range(1,len(s)//2+1):
#         l=[]
#         for j in range(0, len(s), size):
#             l.append(s[j:j+size])
        

#         ans=0
#         cnt=1
#         for i in range(len(l)):         
#             if i==0:
#                 pre=l[0]
#                 cnt=1
#                 continue
                
#             cur=l[i]            
#             if pre == cur:
#                 cnt+=1
#             else:
#                 if cnt==1:
#                     cnt=""
#                 ans+=len(str(cnt))+len(pre)            
#                 pre=cur
#                 cnt=1
                
#         if cnt==1:
#             cnt=""
#         ans+=len(str(cnt))+len(pre)   

#         answer=min(answer,ans)
#     return answer