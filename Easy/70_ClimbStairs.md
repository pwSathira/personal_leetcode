### Monday, November 4th 2024, 8:31 pm

### Problem
Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.

**Example 1:**

**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]

---
### Solution
```
class Solution {

    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        generateCombinations(result, "", 0, 0, n);
        return result;
    }

    public static void generateCombinations(List<String> result, String s, int open, int close, int max){
        //If complete one set of parenthesis
        if (s.length() == max*2){
            result.add(s);
            return;
        }
        if (open < max){
            generateCombinations(result, s + "(", open + 1, close, max);
        }
        if (close < open){
             generateCombinations(result, s + ")", open, close + 1, max);
        }
    }
}
```


