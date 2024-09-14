### Saturday, September 14th 2024, 10:33 am

### Problem

*Given a string s, find the length of the longest substring without repeating characters.* 
#### Example 1
>**Input:** s = "abcabcbb"
>**Output:** 3
>**Explanation:** The answer is "abc", with the length of 3.

---
### Solution
```
Initial Solution

class Solution{

    public int lengthOfLongestSubstring(String s){
        int sLength = s.length();
        int longestLength = 0;
        for(int i = 0; i<sLength; i++){
            int currentLongest = 0;
            for(int j = 1; j<sLength-1; j++){
                currentLongest++;
                if(s.charAt(j) == s.charAt(i)){
                    if(currentLongest>longestLength){
                        longestLength = currentLongest;
                    }
                    break;
                }
            }
        }
        return longestLength;
    }
}
```

The problem in this approach is that even though it provides the correct answers to "abcabcbb" and "bbbbb", for string "pwwkew" it fails to do so. The reason is that my algorithm only compares two characters. For example is looks for p to be repeating, but in this case w is the character repeating but it dosen't account for that.

```
Revised Solution

class Solution{
	public int lengthOfLongestSubstring(String s){
	    int sLength = s.length();
        int longestLength=0;
        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int right = 0;
        while (right < sLength){
            if(!charSet.contains(s.charAt(right))){
                charSet.add(s.charAt(right));
                longestLength = Math.max(longestLength, right-left+1);
                right++;
            } else {
                charSet.remove(s.charAt(left));
                left++;
            }
        }
        return longestLength;
	    }
	}
}
```

In this solution instead of using two separate for loops, I used a HashSet, which only contains unique characters, and a while loop. Here I use a sliding window algorithm, we start at the beginning of the string at a window size of 0. And as we check if the next character in the string is contained in the charSet we see if the longestLength has increased, and increase the size of the window. If not we move the window along from the left and continue searching. 