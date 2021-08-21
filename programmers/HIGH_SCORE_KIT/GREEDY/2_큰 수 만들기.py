#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
   
    ans=[]
    for e in number:

        while len(ans)>0 and e>ans[-1] and k>0:
            ans.pop()
            k-=1
        
        ans.append(e)

    answer="".join(ans[0:len(number)-k])
    return answer