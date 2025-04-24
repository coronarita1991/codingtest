class Solution {
    
    public static int maxSticker(int[] arr){
        int n = arr.length;
        if (n==1) return arr[0];
        
        int[] dp = new int[n];
        dp[0] = arr[0];
        dp[1] = Math.max(arr[0], arr[1]);
        
        for (int i=2; i<n; i++){
            dp[i] = Math.max(dp[i-1], dp[i-2] + arr[i]);
        }
        
        return dp[n-1];
    }
    
    
    public int solution(int sticker[]) {
        int n = sticker.length;
        if (n == 1) return sticker[0];        
       
        int[] case1 = new int[n-1];
        System.arraycopy(sticker, 0, case1, 0, n-1);
        int[] case2 = new int[n-1];
        System.arraycopy(sticker, 1, case2, 0, n-1);
        
        return Math.max(maxSticker(case1), maxSticker(case2));
    }
}