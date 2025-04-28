def solution(n):
    answer = ''
    
    if n == 1 : 
        return '1'
    
    num_map = {
        0 : '1',
        1 : '2',
        2 : '4',
    }
    
    while n > 0 :
        n -= 1
        mod = n%3        
        answer = num_map[mod] + answer
        n //= 3

        
    return answer 