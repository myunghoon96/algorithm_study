# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    usr_dic = defaultdict(set)
    mail_dic = defaultdict(int)
    for e in report:
        report_usr, reported_usr = e.split()
        usr_dic[reported_usr].add(report_usr)

    for key,val in usr_dic.items():
        if len(val) >= k :
            # print(key, " BAN")
            for v in val:
                mail_dic[v] += 1
    # print(mail_dic) 
    for id in id_list:
        answer.append(mail_dic[id])
    return answer