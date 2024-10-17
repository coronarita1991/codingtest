class Solution:
    # sol2. Memoization
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if N <= 1:
            return N
        
        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N-1) + self.fib(N-2)
        return self.dp[N]
    
        # # sol1. Tabulation
        # fibo = [0] * (n+1)

        # fibo[0] = 0
        # if n == 0:
        #     return fibo[0]

        # fibo[1] = 1
    
        # for i in range(2, n+1):
        #     fibo[i] = fibo[i-1] + fibo[i-2]
        
        # return fibo[n]