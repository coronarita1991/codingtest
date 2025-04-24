def solution(sticker):
    
    N = len(sticker)
    
    # 예외처리 : 1개일 때 
    if N == 1 : 
        return sticker[0]
    
    # DP함수 정의
    def max_sticker(arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        if len(arr) > 1 :
            dp[1] = max(arr[0], arr[1])
        
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        
        return dp[-1]
    
    # case1 : 첫번째 스티커 포함
    case1 = max_sticker(sticker[:-1])
    # case2 : 마지막 스티커 포함
    case2 = max_sticker(sticker[1:])
    
    return max(case1, case2)