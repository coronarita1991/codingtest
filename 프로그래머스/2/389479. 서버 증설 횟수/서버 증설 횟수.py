import math

def solution(players, m, k):
    n = len(players)
    answer = 0
    active = [0] * (n + k) # active[i] : 시간 i에 몇 대의 서버가 켜져있는지
    
    for i in range(n):
        need = math.floor(players[i] / m)
        
        if active[i] >= need:
            continue
        
        add = need - active[i]
        answer += add
        
        # 서버 j 동안 켜있어야 됨
        for j in range(i, i+k):
            active[j] += add
            
    
    return answer