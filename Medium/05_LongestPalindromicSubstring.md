### Wednesday, September 18th 2024, 11:54 am

### Problem
*_Given a string `s`, return the longest palindromic substring in `s`._
#### Example 1:
> **Input:** `s = "babad"`  
> **Output:** `"bab"  
> **Explanation:** `aba` is also a valid answer.

#### Example 2:
> **Input:** `s = "cbbd"`  
> **Output:** `"bb"`
---
### Solution
```
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int start = 0;
        int end = 0;
        int maxLen = 1;
        if (n <= 1){ return s; }
        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++){
            dp[i][i] = true;
            for (int j = 0; j < i; j++){
                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || dp[j + 1][i - 1])) {
                    dp[j][i] = true;
                    if (i - j + 1 > maxLen){
                        maxLen = i - j + 1;
                        start = j;
                        end = i;
                    }
                }
            }
        }
        return s.substring(start, end + 1);
    }
}
```

Initially my first approach was to start from the middle and iteratively expand from the center and check  if the surrounding letters from center matched. I check for both odd and even, this lead to taking too much time for the leetcode compiler to submit. I then used the solution from leetcode to learn what solution to use.
