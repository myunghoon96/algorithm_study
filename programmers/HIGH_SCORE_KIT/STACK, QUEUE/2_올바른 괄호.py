# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True

    def is_pair():
        left_cnt = 0
        for e in s:
            if e == "(":
                left_cnt += 1
            else:
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    return False

        if left_cnt != 0:
            return False

        return True

    return is_pair()
