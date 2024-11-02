### Friday, November 1st 2024, 9:47 pm

### Problem
Given an integer `x`, return `true` _if_ `x` _is a_ _**palindrome**__, and_ `false` _otherwise_.

**Example 1:**

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

---
### Solution
```
class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int sLength = s.length();
        //Only have to check till middle, therefore n/2
        for (int i = 0; i < sLength/2; i++){
            if (s.charAt(i) != s.charAt(sLength-i-1)){
                return false;
            }
        }
        return true;
    }
}
```


