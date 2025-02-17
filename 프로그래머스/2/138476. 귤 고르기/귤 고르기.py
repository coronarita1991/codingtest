def solution(k, tangerine):
    answer = 0
    
    # 10,000,000개 - 단일 반복으로 처리해야 함.
    # 서로다른 종류의 수가 최소
    
    from collections import Counter
    info = Counter(tangerine)
    
    # 경계값 처리
    if k == 1 :
        return 1
    elif k == len(tangerine):
        return len(info)
    
    
    for idx, (_, v) in enumerate(sorted(info.items(), key=lambda x: -x[1])):
        # print(idx,  _,  v, k)
        k -= v
        
        if k <= 0: 
            answer = idx
            break
    
    return answer+1