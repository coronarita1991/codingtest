from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0
    
    for i in range(100, 1001):
        if counter[i] > 0 : 
            answer += counter[i] * (counter[i]-1) // 2 # nC2
            answer += counter[i] * counter[i*2] # 1:2
            answer += counter[i] * counter[2*i/3] # 2:3
            answer += counter[i] * counter[3*i/4] # 3:4

    return answer