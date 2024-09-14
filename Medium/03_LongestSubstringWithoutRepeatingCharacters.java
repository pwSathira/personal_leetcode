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