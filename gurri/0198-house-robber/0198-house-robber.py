class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            # 한집 걸러서 방문
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return max(dp)