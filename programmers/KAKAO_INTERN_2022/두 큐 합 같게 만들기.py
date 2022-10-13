# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    answer = 0
    ttl = sum(queue1) + sum(queue2)
    half = ttl // 2

    l, r = 0, len(queue1)-1
    nums = queue1 + queue2
    cnt = 0
    sum_q1 = sum(queue1)

    while True:
        if cnt > len(nums) * 2:
            answer = -1
            break

        if sum_q1 == half:
            answer = cnt
            break

        elif sum_q1 < half:
            r += 1
            if r == len(nums):
                r = 0
            cnt += 1
            sum_q1 += nums[r]

        elif sum_q1 > half:
            sum_q1 -= nums[l]
            l += 1
            if l == len(nums):
                l = 0
            cnt += 1

    return answer
