# https://www.acmicpc.net/problem/21776
import copy
import sys
from collections import defaultdict

N, C = map(int, sys.stdin.readline().split())
submits = [list(sys.stdin.readline().split()) for _ in range(N)]
ops = [sys.stdin.readline().rstrip().split(',') for _ in range(C)]

answers = []
cnt_dic = defaultdict(int)
person_ops = defaultdict(list)

works = []
for i, submit in enumerate(submits):
    cnt = int(submit[0])
    cards_idxs = submit[1:]
    cnt_dic[i] = cnt
    works += [i]*cnt
    for card_idx in cards_idxs:
        card_idx = int(card_idx) - 1
        person_ops[i].append(ops[card_idx])

works_orders = []
def make_orders(depth, order_list):
    if depth == C:
        works_orders.append(order_list)
        return

    for person in range(N):
        if order_list[:depth].count(person) < cnt_dic[person]:
            copy_order_list = copy.deepcopy(order_list)
            copy_order_list[depth] = person
            make_orders(depth + 1, copy_order_list)

make_orders(0, [-1] * C)

for work_order in works_orders:
    idx_dic = defaultdict(int)
    tmp_result = ""

    error_flag = False
    for person in work_order:
        cur_ops = person_ops[person][idx_dic[person]]
        idx_dic[person] += 1
        
        if error_flag:
            break

        for cur_op in cur_ops:
            instruction, value = cur_op.split()
            if instruction == "ADD":
                tmp_result += value
            else:
                if int(value) >= len(tmp_result) or len(tmp_result) == 0:
                    tmp_result = "ERROR"
                    error_flag = True
                    break
                tmp_result = tmp_result[:i] + tmp_result[i+1:]
        

    if tmp_result == "":
        tmp_result = "EMPTY"

    answers.append(tmp_result)

answers =sorted(list(set(answers)))

for e in answers:
    print(e)