### Monday, November 11th 2024, 8:29 pm

### Problem
Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest** 

**palindrome**

 that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

**Example 1:**

**Input:** s = "abccccdd"
**Output:** 7
**Explanation:** One longest palindrome that can be built is "dccaccd", whose length is 7.

---
### Solution
```
public class LongestPalindrome {
    public int longestPalindrome(String s) {
        // HashMap to count occurrences of each character
        HashMap<Character, Integer> charCount = new HashMap<>();
        
        // Count frequencies of each character
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        int palindromeLength = 0;
        boolean oddFound = false;
        
        // Calculate the length of the longest palindrome
        for (int count : charCount.values()) {
            if (count % 2 == 0) {
                // Add all even counts
                palindromeLength += count;
            } else {
                // Add the largest even part of odd counts
                palindromeLength += count - 1;
                oddFound = true;
            }
        }
        
        // If any odd character count exists, we can place one in the center
        if (oddFound) {
            palindromeLength += 1;
        }
        
        return palindromeLength;
    }
```


