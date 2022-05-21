from multiprocessing.connection import answer_challenge


n, k = 5, 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

a.sort()
b.sort(reverse=True)

for i in range(n):
    if a[i] < b[i] and k > 0:
        k -= 1
        a[i] = b[i]

print(sum(a))

# a.sort(reverse= True)
# b.sort(reverse= True)

# i, j = 0, 0
# cnt = 0
# ans = 0
# while cnt != n:
#     if a[i] >= b[j]:
#         ans += a[i]
#         cnt += 1
#         i+=1
#     else:
#         if k > 0:
#             ans += b[j]
#             k -= 1
#             j += 1
#         else:
#             ans += a[i]
#             i += 1    
            
#         cnt += 1

# print(ans)