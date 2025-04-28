def inspect(stones, p, k):
    cnt = 0
    for s in stones:
        # p명이 지난 후 s-p ≤ 0 이면 0 칸
        if s <= p:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    answer = 0
    
    # 이진 탐색
    s = 1
    e = max(stones)
    
    while s <= e: 
        mid = (s+e) // 2
        
        # 가능하다면
        if inspect(stones, mid, k) :
            s = mid + 1            
        # 불가능하다면
        else :
            e = mid - 1
    
    return s