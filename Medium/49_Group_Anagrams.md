### Friday, September 20th 2024, 4:12 pm

### Problem
__Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.__
#### Example 1:
> **Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`  
> **Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`  
> **Explanation:**  
> There is no string in `strs` that can be rearranged to form "bat".  
> The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.  
> The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#### Example 2:
> **Input:** `strs = [""]`  
> **Output:** `[[""]]`
#### Example 3:
> **Input:** `strs = ["a"]`  
> **Output:** `[["a"]]`
---
### Solution
```
import java.util.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGroups = new HashMap<>();
        for (String s : strs) {
            String sorted = sortArrEquiv(s);
            if (!anagramGroups.containsKey(sorted)) {
                anagramGroups.put(sorted, new ArrayList<>());
            }
            anagramGroups.get(sorted).add(s);
        }
        return new ArrayList<>(anagramGroups.values());
    }
    public String sortArrEquiv(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }
}
```

This solution was fairly easy, it required a Map of String, and List<String>. The string for the key value was the sorted character string, and then checked it against other strings by sorting it and then seeing if it matches the key.

