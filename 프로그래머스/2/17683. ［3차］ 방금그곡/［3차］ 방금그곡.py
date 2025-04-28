def inspect(total, partial):
    # partial이 total의 내에 있으면 True 반환
    len_p = len(partial)

    for idx in range(len(total) - len_p+1):
        if ''.join(partial) == ''.join(total[idx:idx+len_p]):
            return True
    return False

def solution(m, musicinfos):
    import re
    
    pattern = r'[A-Z]#?'
    input_m = re.findall(pattern, m)
    m_length = len(input_m) # 음악 길이
    
    answer = []
    
    # info순회
    for idx, musicinfo in enumerate(musicinfos) :
        
        start_time, end_time, song_name, m_info = musicinfo.split(',')
        
        # 재생 시간
        e_hh, e_mm = map(int, end_time.split(':'))
        s_hh, s_mm = map(int, start_time.split(':'))
        # if e_hh == 0 and e_mm > 0 : 
        #     e_hh = 23
        #     e_mm = 59
        play_time = (e_hh - s_hh) * 60 + (e_mm - s_mm)
        
        # t2 = end_time
        # t1 = start_time
        # from datetime import datetime as dt
        # play_time = int((dt.strptime(t2,'%H:%M')-dt.strptime(t1,'%H:%M')).total_seconds()//60)

        
        # 음악 내용
        notes = re.findall(pattern, m_info)
        
        played = []
        # 재생된 시간 > 음악길이 : 
        for t in range(play_time):
            played.append(notes[t % len(notes)])
        
        if inspect(played, input_m):        
            # 비교 : 재생 시간 내림차순 / 순서 오름차순
            answer.append((play_time, idx, song_name))
        
    answer.sort(key=lambda x: (-x[0], x[1]))
    # print(answer)
    
    if len(answer) == 0 :
        return "(None)"
    
    if not answer : 
        return "(None)"
    
    return answer[0][-1]