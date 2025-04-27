def calc_time(level, diffs, times):
    
    elapsed = 0
    
    for idx, (diff, time_cur) in enumerate(zip(diffs, times)):
        if diff <= level:
            elapsed += time_cur
        else :
            elapsed += (diff - level) * (time_cur + times[idx - 1]) + time_cur
            
    # print(level, elapsed)
    return elapsed
    
def solution(diffs, times, limit):
    answer = 0
    
    
    # 최소 숙련도 lv를 탐색해야 함. 1 - 300_000개
    # 숙련도의 최댓값 = 100_000개 => 시간복잡도 : 3*10^10 최악 -> parametric search 적용
    
    s = 1
    e = max(diffs)
    
    # 시간 만족하는 최솟값 구해야 함.
    # 이분 탐색
    while s <= e :
        mid = (s + e) // 2
        
        # 조건 확인
        if calc_time(mid, diffs, times) > limit :
            s = mid + 1
        else : 
            answer = mid
            e = mid - 1
            
    return answer