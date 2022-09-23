# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    kind = len(set(nums))
    choose = len(nums)//2

    return min(kind, choose)
