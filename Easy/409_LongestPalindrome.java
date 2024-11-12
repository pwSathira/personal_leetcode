class Solution {
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
}