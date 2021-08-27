#https://programmers.co.kr/learn/courses/30/lessons/17683


def solution(m, musicinfos):
    answer = ''
    ansPlayTime = 0

    m=m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a").replace("B#","b")

    for e in musicinfos:
        t1, t2, title, info = e.split(',')
        start=int(t1[0:2])*60+int(t1[3:])
        end=int(t2[0:2])*60+int(t2[3:])
        playTime=end-start
        
        info = info.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a").replace("B#","b")

        
        melody=(info*(playTime//len(info)+1))[:playTime]

        if m in melody:
            if answer == '':
                answer=title
                ansPlayTime=playTime
            else:
                if ansPlayTime<playTime:
                    answer=title
                    ansPlayTime=playTime

                    
    if answer=='':
        answer="(None)"
        
    return answer