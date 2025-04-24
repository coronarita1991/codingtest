def solution(storey):
    answer = 0
    
    # 자릿수가 5 이하 : 아래로
    # 5 초과 : 위로
    
    while storey > 0 : 
        mod = storey%10
        if mod > 5 : 
            answer += 10 - mod 
            storey = storey//10 + 1
        elif mod < 5 : 
            answer += mod 
            storey = storey//10
            
        else : 
            # mod = 5
            # 다음 자리까지 확인
            nxt = (storey // 10) % 10
            
            if nxt >= 5 : 
                answer += 10 - mod 
                storey = storey//10 + 1
            else : 
                answer += mod 
                storey = storey//10
            
    
    return answer