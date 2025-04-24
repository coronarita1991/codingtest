def solution(n):
    answer = []
    
    if n == 1:
        return [1]
    
    dirs = [[1,0], [0,1], [-1, -1]]
    d = 0
    
    arr = [[0]*i for i in range(1, n+1)]
    num = 1
    x, y = 0, 0
    while arr[x][y] == 0 :
        # 값 채워넣고
        arr[x][y] = num
        
        # 다음 방향으로 이동 
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]
        
        def in_range(x, y):
            return 0<=x<n and 0<=y<n
        
        if not in_range(nx, ny) or arr[nx][ny] :
            d = (d+1)%3
            nx = x + dirs[d][0]
            ny = y + dirs[d][1]
        
        x, y = nx, ny
        num+=1

    for elem in arr:
        answer.extend(elem)
        
    return answer

# print(solution(1))
print(solution(2))
print(solution(3))