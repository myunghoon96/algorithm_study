#https://programmers.co.kr/learn/courses/30/lessons/17678

def minute_to_time(minute):
    hh=minute//60
    mm=minute%60
    return str(hh).zfill(2)+str(":")+str(mm).zfill(2)

def solution(n, t, m, timetable):
    answer = ''
    bus_times = []
    start_time = 9*60
    total_people = len(timetable)
    people_times = []
    finish_people = 0
    
    for e in timetable:
        hh, mm = int(e[0:2]), int(e[3:5])
        people_times.append(hh*60+mm)  
    people_times.sort()
#     print("people_times", people_times)
    
    for i in range(n):
        bus_times.append(start_time+ i*int(t))
#     print("bus_times", bus_times)
    
#     print("m",m)
    last_bus_time = start_time + (n-1)*t
    # print("last_bus_time",last_bus_time)
    
    #except last bus
    for bus_index in range(len(bus_times)-1):
        bus_time = bus_times[bus_index]
        endBoundary = finish_people+m if finish_people+m<total_people else total_people
        for i in range(finish_people, endBoundary):
            if people_times[i] <= bus_time:
                # print("!!FINISH ", people_times[i], bus_time)
                finish_people+=1
                
    # print("finish_people", finish_people)
    
    left_people = len(timetable)-finish_people
    # print("left_people", left_people)
    
    if left_people < m:
        answer = last_bus_time
    
    else:
        if total_people > finish_people-1+m:
            last_success_people_time = people_times[finish_people-1+m]
#             print("last_success_people_time ", last_success_people_time)
        
#         print("last_bus_time", last_bus_time)
        
        if last_bus_time < last_success_people_time:
            answer = last_bus_time
        else:
            answer = last_success_people_time -1
    
    answer = minute_to_time(answer)
    # print("answer ", answer)
    return answer