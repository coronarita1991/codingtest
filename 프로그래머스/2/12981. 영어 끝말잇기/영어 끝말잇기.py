def solution(n, words):
    answer = []
    vis = set()
    flag = False
    buffer = ""
    
    # 가장 먼저 탈락하는 사람, 그 사람이 몇 번째 차례에 탈락하는 지 
    for idx, word in enumerate(words):
        # 끝말잇기 조건 : 중복 혹은 불만족
        if idx == 0 :
            vis.add(word)
            buffer = word
            continue
        
        if word[0] != buffer[-1] or word in vis : 
            flag = True
            answer.append(idx%n+1)
            answer.append(idx//n+1)
            break
        
        
        # 
        vis.add(word)
        buffer = word
    
    if not flag:
        answer = [0, 0]
    
        
    return answer