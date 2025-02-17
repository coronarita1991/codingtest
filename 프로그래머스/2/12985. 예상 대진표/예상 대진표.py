def solution(n,a,b):
    answer = 1
    
    if a > b : a, b = b, a # a < b로 생각하고 진행 
    # offset
    a -= 1
    b -= 1
    
    while a != b :
        div_a = a // 2
        div_b = b // 2
        if div_a == div_b : 
            break
        a, b = div_a, div_b
        answer += 1
    
    
    
    return answer