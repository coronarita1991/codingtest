#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSticker(vector<int> arr){
    int n = arr.size();
    vector<int> dp(n);
    
    dp[0] = arr[0];
    dp[1] = max(arr[0], arr[1]);
    
    for (int i=2; i<n; i++){
        dp[i] = max(dp[i-1], dp[i-2] + arr[i]);
    }
    
    return dp[n-1];
}

int solution(vector<int> sticker)
{
    int n = sticker.size();
    if (n==1) return sticker[0];
    
    vector<int> case1(sticker.begin(), sticker.end()-1);
    vector<int> case2(sticker.begin()+1, sticker.end()); 

    return max(maxSticker(case1), maxSticker(case2));
}