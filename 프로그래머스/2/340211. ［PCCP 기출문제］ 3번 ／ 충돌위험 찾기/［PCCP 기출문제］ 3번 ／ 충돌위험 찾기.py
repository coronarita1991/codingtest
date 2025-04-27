def solution(points, routes):
    answer = 0
    
    # 각 routes 이동 결과를 traces에 저장
    traces = dict()
    
    for idx, route in enumerate(routes, start = 1) : 
        sub_trace = []
        for j, point_num in enumerate(route):
            # 각 route를 진행해야 함
            if j < len(route)-1:
                cx, cy = points[point_num - 1]
                tx, ty = points[route[j+1]-1]
                
                dx = 1 if tx > cx else -1
                dy = 1 if ty > cy else -1
                
                while cx != tx: 
                    sub_trace.append((cx, cy))
                    cx += dx
                    
                while cy != ty: 
                    sub_trace.append((cx, cy))
                    cy += dy
            else : 
                cx, cy = points[point_num - 1]
                sub_trace.append((cx, cy))
                    
            
        traces[idx] = sub_trace
    
    # traces들을 시간 순으로 체크하면서 중복여부 확인
    max_time = max([len(v) for v in traces.values()])
    
    from collections import Counter
    
    for t in range(max_time):
        counter = Counter()
        
        for v in traces.values():
            if t < len(v): # 필터 걸기 - 각 리스트 길이 초과하지 않는다면 카운터에 계수
                counter[v[t]] += 1
        
        for c in counter.values():
            if c >= 2: 
                answer += 1
        
        # print(counter)
                
    
    
    
    return answer