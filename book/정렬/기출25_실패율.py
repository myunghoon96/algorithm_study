# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    answers = []

    for i in range(1, N+1):
        stop = stages.count(i)
        reach = 0
        for e in stages:
            if e >= i:
                reach += 1

        if reach == 0:
            failure = 0
        else:
            failure = stop/reach
        answers.append((failure, i))

    answers.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    for e in answers:
        answer.append(e[1])

    return answer
