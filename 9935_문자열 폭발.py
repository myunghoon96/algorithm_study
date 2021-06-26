#https://www.acmicpc.net/problem/9935

s=input()
p=input()

l=[]

for i in range(len(s)):
    l.append(s[i])
    if l[-1]==p[-1]:

        if ''.join(l[-len(p):])==p:
            del l[-len(p):]
if len(l)==0:
    print("FRULA")
else:
    print(''.join(l))