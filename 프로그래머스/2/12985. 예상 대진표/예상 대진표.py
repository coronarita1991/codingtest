def solution(n,a,b):
    answer = 1
    
    # if a > b : a, b = b, a # a < b로 생각하고 진행 
    # # offset
    a -= 1
    b -= 1
    
    while a != b :
        if a // 2 == b // 2 : 
            break
        a, b = a // 2, b // 2
        answer += 1
    
    
    
    return answer