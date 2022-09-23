# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []

    for e in arr:
        if answer[-1:] == [e]:
            continue
        else:
            answer.append(e)

    return answer

#     def next_num():
#         pop_element = arr.pop()
#         while arr:
#             if arr[-1] == pop_element:
#                 arr.pop()
#             else:
#                 break
#         return pop_element

#     while arr:
#         answer.append(next_num())

#     return answer[::-1]
