# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

from collections import defaultdict


def solution(survey, choices):
    answer = ''
    score_dic = defaultdict(int)

    def get_character(a, b):
        if score_dic[a] >= score_dic[b]:
            return a
        return b

    for idx, choice in enumerate(choices):
        if 1 <= choice <= 3:
            score_dic[survey[idx][0]] += (4 - choice)
            pass
        elif choice > 4:
            score_dic[survey[idx][1]] += (choice - 4)
    # print(score_dic)

    answer += get_character('R', 'T')
    answer += get_character('C', 'F')
    answer += get_character('J', 'M')
    answer += get_character('A', 'N')

    return answer
