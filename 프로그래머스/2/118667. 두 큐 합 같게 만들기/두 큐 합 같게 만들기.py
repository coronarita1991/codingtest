def solution(queue1, queue2):
    answer = -2
    from collections import deque
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    
    for i in range((len(queue1)+len(queue2))*2):
        if tot1 == tot2 :
            
            answer = i
            break
        elif len(queue1) and tot1 > tot2 :
            elem = queue1.popleft()
            tot1 -= elem
            tot2 += elem
            queue2.append(elem)
        elif len(queue2):
            elem = queue2.popleft()
            tot2 -= elem
            tot1 += elem
            queue1.append(elem)
        # print(queue1, queue2)   
    if answer == -2 :
        return -1
    else :
        return answer
