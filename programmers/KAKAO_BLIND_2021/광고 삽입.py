#https://programmers.co.kr/learn/courses/30/lessons/72414

def solution(play_time, adv_time, logs):
    answer = ''
    def time_to_sec(time):
        h,m,s = time.split(":")
        return int(h)*3600+int(m)*60+int(s)
    def sec_to_time(time):
        h=time//3600
        m=time%3600//60
        s=time%3600%60
        return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    
    total_sec = [0 for _ in range(play_sec+1)]
    for log in logs:
        start, end = log.split("-")
        total_sec[time_to_sec(start)]+=1
        total_sec[time_to_sec(end)]-=1
    
    for i in range(1, play_sec+1):
        total_sec[i] += total_sec[i-1]
    
    for i in range(1, play_sec+1):
        total_sec[i] += total_sec[i-1]
    
    ans_view=total_sec[adv_sec]
    ans_start=0
    for start in range(1, play_sec+1):
        if start+adv_sec>=play_sec:
            end = play_sec
        else:
            end = start+adv_sec
            
        if ans_view < total_sec[end] - total_sec[start]:
            ans_view = total_sec[end] - total_sec[start]
            ans_start = start+1
    
    answer=sec_to_time(ans_start)
    return answer