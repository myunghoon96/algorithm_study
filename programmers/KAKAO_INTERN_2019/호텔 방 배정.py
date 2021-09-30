#https://programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(10000000)

def find_empty(num, rooms):
    if rooms.get(num) == None:
        rooms[num] = num + 1
        return num
    
    empty_num = find_empty(rooms[num], rooms)
    rooms[num] = empty_num + 1
    return empty_num
    
def solution(k, room_number):
    answer = []
    rooms = dict()

    for num in room_number:
        answer.append(find_empty(num, rooms))
   
    return answer